#!/usr/bin/env python3
'''
Logs into ... email web site with the provided
username and password (in the "username" and "pwd" variables below)
sends email with provided subject to the provided email address
from the command line
Usage: cme e-address subject'
"cme" is the alias for this program to run on my computer
It has to be defined at least once separately if this program is run
on another computer.
'''
'''
Write a program that takes an email address and string of text on the
command line and then, using Selenium, logs into your email account and
sends an email of the string to the provided address. (You might want
to set up a separate email account for this program.)
'''

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

logging.basicConfig(level=logging.INFO,\
                    format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.WARNING)

logging.warning('Start of program')


message = 'This message is sent using Selenium.'

# check if information is provided
if len(sys.argv) < 3:
    print('Usage: cme e-address subject')
    sys.exit()

# check if email address is proper
emDiv = sys.argv[1].split('@')
if len(emDiv) != 2 or emDiv[0] == '' or emDiv[1] == '': 
    print('Invalid e-mail address:', sys.argv[1])
    print('Usage: cme e-address subject')
    sys.exit()

toAddress = sys.argv[1]
subject = ' '.join(sys.argv[2:])

username = '...' # login name for the from email address
pwd = '...' # associated password with the login name
emailSite = 'https://...' # web interface address
                                            # for the email server

print(f'Will send email to {toAddress} with subject '\
      f'"{subject}" from "{username}"')

# open browser based on the operating system my computer is using
# this became necessary as IDLE on mac OS on my computer can not
# locate the geckodriver
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

# login to email server 
browser.get(emailSite)
unElem = browser.find_element_by_id('loginuser')
unElem.send_keys(username) 
passElem = browser.find_element_by_id('loginpwd')
passElem.send_keys(pwd) 
subElem = browser.find_element_by_name("submit")
subElem.click() # passwordElem.submit() does not work probably
                # due to poor coding at email server web interface.

newMailElem = browser.find_element_by_class_name('compose')
newMailElem.click()

# For no obvious reason, code unable to get to create new email  
# window even after clicking on compose new message sometimes.
# Probably the page opened is focused somewherelse on new mail
# checking at times and this prevents the compose button from
# functioning properly. But I have not been able to clearly  
# understand the mechanism creating the problem yet. I have
# resorted to 100% working but still stopgap measures to resolve the
# problem.
try:
    toMailElem = browser.find_element_by_name('_to')
    toMailElem.send_keys(toAddress)
except Exception as errMsg:
    eMsg = errMsg.args[0].strip('\n')
    logging.error(f'Warning: exception "{eMsg}" encountered.\n'\
                  'Will create new email window directly.')
    # executing new mail command directly whenever new mail window
    # could not be opened
    compCom = newMailElem.get_attribute('href')
    browser.get(compCom)
    toMailElem = browser.find_element_by_name('_to')
    toMailElem.send_keys(toAddress)


subMailElem = browser.find_element_by_name('_subject')
subMailElem.send_keys(subject) # enter email subject

bodyMailElem = browser.find_element_by_id('composebody_ifr')
bodyMailElem.send_keys(message) # enter email body

sendMailElem = browser.find_element_by_id('rcmbtn114')
sendMailElem.click() # send the message

closeMailElem = browser.find_element_by_css_selector('#rcmbtn103')
closeMailElem.click() # log out

browser.quit()

print('Email sent!')
