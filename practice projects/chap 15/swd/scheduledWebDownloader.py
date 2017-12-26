#!/usr/bin/env python3
''' Write a program that checks the websites of several web comics and
automatically downloads the images if the comic was updated since the
program’s last visit. Your operating system’s scheduler (Scheduled Tasks
on Windows, launchd on OS X, and cron on Linux) can run your Python
program once a day. The Python program itself can download the comic and
then copy it to your desktop so that it is easy to find. This will free
you from having to check the website yourself to see whether it has
updated.
'''

import os
import bs4
import requests

# Get the names of the XKCD picture files on your computer
r'''
# Notice how the string is prefixed with r to make Pyton
# understand it as a raw string. Otherwise needs to backslash all
# backslashes followed by 'U' or 'x' here.
dirPath = 'C:\Users\Alper\iCloudDrive\Documents\Python' + \
        '\Automate the boring stuff\quizzes\practice projects' + \
        '\Chap 15\xkcd'
'''


dirPath = '/Users/Alper/Library/Mobile Documents/' + \
        'com~apple~CloudDocs/documents/python/' + \
        'Automate the boring stuff/quizzes/practice projects' + \
        '/chap 15/xkcd'

dirPath = os.path.abspath(dirPath) # make sure it is absolute

# Script stopped if directory does not exist
assert os.path.exists(dirPath) == True, f'directory {dirPath} does'  + \
        'not exist'

os.chdir(dirPath)
imgFilenames = []  # existing image filenames 
for filename in os.listdir('.'):
    imgFilenames += [filename]
 
'''
Get name of most recent picture file from XKCD and download it if it
does not already exist.

Do this also for the next four most recent picture files on XKCD as well
'''

url = 'http://xkcd.com'  # starting url
noHist = 5 # highest number of images to be checked
noDown = 0
print(f'Scanning page {url}... for new images')

for i in range(noHist):
    # Download the page.
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:  # If no comic, look for next one
        print('Could not find comic image.')
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'http://xkcd.com' + prevLink.get('href')
        continue
    else:  # normal proceeding of flow
        try:
            comicUrl = 'http:' + comicElem[0].get('src')
            if os.path.basename(comicUrl) in imgFilenames:
                break  # Exit download loop as new images downloaded
            # Download the image because it is new
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            ''' skip this comic if can not be downloaded and
            look for next one
            '''
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # Save downloaded image to disk
    imageFileObj = open(os.path.basename(comicUrl), 'wb')
    for chunk in res.iter_content(100000):
        imageFileObj.write(chunk)
    imageFileObj.close()
    noDown += 1

    # Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print(f'{noDown} new image(s) downloaded')

# this is for archival purposes
#!Library/Frameworks/Python.framework/Versions/3.6/bin/python3
