#!/usr/bin/env python3
'''
Downloads all images in the specified category from imgur.com
to the specified directory.
Gets the number of images found and asks for confirmation before
starting the download.
Imgur shows only 60 posts found at most at first.
User needs to push the browser downward to get more
but this push not stimulated here.
Therefore the max you can get is 60 posts for a search via this code
Works only from from the command line
Usage: imgur <dir_name> <keyword(s)>'
'''
'''
Write a program that goes to a photo-sharing site like Flickr or Imgur,
searches for a category of photos, and then downloads all the resulting
images. You could write a program that works with any photo site that
has a search feature.
'''

import logging
import os
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time

logging.basicConfig(level=logging.WARNING,\
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

logging.info('Start of program')

def pec(msg='press Enter to continue or "q" to quit'):
# implements 'press Enter to continue'
# returns the character entered
    ch = ''
    while ch == '':
        print(msg)
        ch = sys.stdin.read(1)
    return ch


# check if information is provided
if len(sys.argv) < 3:
    print('Usage: imgur.py <folder_name> <keyword(s)>')
    sys.exit()

folderName = sys.argv[1]
keywords = ' '.join(sys.argv[2:])

# open browser based on the operating system my computer is using
# this became necessary as IDLE on mac OS can not locate the geckodriver
# no such issue when interpreted directly by Python interpreter via
# the command line 
if sys.platform == 'win32':
    browser = webdriver.Firefox()
elif sys.platform == 'darwin': # mac OS
    browser = webdriver.Firefox(\
        executable_path=\
        '/usr/local/Cellar/geckodriver/0.19.0/bin/geckodriver')
else:
    print('Warning - Unknown OS:', sys.platform)
    print('Assuming geckodriver can be accessed properly'\
          'by the Python interpreter.')
    browser = webdriver.Firefox()

# Search imgur for a category of photos
browser.get('https://www.imgur.com')
searchElem = browser.find_element_by_class_name('icon-search')
searchElem.click()
searchElem.send_keys(keywords)
searchElem.submit()

time.sleep(2) # extra waiting for imgur to load images
wait = WebDriverWait(browser, 3)
dumElem = wait.until(EC.title_contains(keywords))
# get the posts with pictures matching the keywords
try:
    postElems = wait.until(EC.presence_of_all_elements_located\
                           ((By.CLASS_NAME, 'post')))
    print(f'{len(postElems)} posts found for "{keywords}"')
except Exception as exc: # exit program if no posts found
    print(f'No posts found for "{keywords}". Try with other keywords.')
    browser.quit()
    sys.exit()
    
# confirm with user to proceed
if pec() == 'q':
    print('program stopped by user')
    browser.quit()
    sys.exit()
print(f'getting and saving pictures under "{folderName}"...')

# Create a directory under the current one if not already there
try:
    os.mkdir(folderName)
except FileExistsError:
    print(f'\nfolder {folderName} already exists')
    if pec('Press Enter to overwrite or "q" to quit') == 'q':
        print('program stopped by user')
        browser.quit()
        sys.exit()          
os.chdir(folderName)

count = 0
for element in postElems:
    # get the picture's properties from imgur
    pictID = element.get_attribute("id")
    try:
        pictElem = browser.find_element_by_css_selector\
                   (f'#{pictID} > a:nth-child(1) > img:nth-child(1)')
    except Exception as exc:
        print(f'\nThere was a problem: {exc}\ncontinuing with next'\
              f' image')
        continue
    mo = re.search('com/(\w+)b\.(\w+)', pictElem.get_attribute('src'))
    fName = mo.group(1) + '.' + mo.group(2)
    print(f'getting file {count + 1}: {fName}')
    pictURL = 'https://i.imgur.com/' + fName
    logging.info(pictURL)

    # get the picture
    res = requests.get(pictURL)
    try:
        res.raise_for_status()
        logging.info(f'file downloaded is {int(len(res.content)/1000):,} kilobytes long')
    except Exception as exc:
        print(f'\nThere was a problem: {exc}\ncontinuing with next'\
              f' image')
        continue

    # save the gotten file
    playFile = open(fName, 'wb')
    tWritten = 0
    for chunk in res.iter_content(10**5):
        # print('{0:,} bytes of data written'.format(playFile.write\
        # (chunk)))
        tWritten += playFile.write(chunk)
    logging.info(f'{int(tWritten/1000):,} kilobytes written in total\n')
    playFile.close()
    count += 1


# Tell user whether the downloads ended successfully or not
print(f'{count} files have been saved under "{os.getcwd()}"')


'''
Example links to posted pictures by imgur
https://imgur.com/gallery/MNJcnuJ - post
https://imgur.com//MNJcnuJ.jpg - regular picture
https://imgur.com//MNJcnuJb.jpg - small picture
https://i.imgur.com/S0uDkfY.jpg - regular picture
https://i.imgur.com/S0uDkfYb.jpg - small picture
https://i.imgur.com/1sHdEF6.jpg - regular picture
'''
