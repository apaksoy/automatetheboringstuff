#!/usr/bin/env python3
''' Chapter 11 showed you how to use the requests module to scrape data
from http://weather.gov/. Write a program that runs just before you wake
up in the morning and checks whether it’s raining that day. If so, have
the program text you a reminder to pack an umbrella before leaving the
house.

This script gets the first full-day verbal weather forecast in Turkish 
at Turkish Meteorological Institute's (MGM) website for Istanbul and
emails it to the specified address.
'''

import getpass

import sys
import smtplib

import bs4
from selenium import webdriver

rain_words = ["yağış", "yağmur", "sağanak"]

# see stackoverflow 45448994 for phantomjs
if sys.platform == 'win32':
  print('Install PhantomJS')
  sys.exit()
elif sys.platform == 'darwin':
# Executable path specified as otherwise PhantomJS headless browser
# does not work.
# Service log path spedified as otherwise script can not be run from
# a .plist file due to the permission problems with the ghostdriver.log
# file.
  browser = webdriver.PhantomJS(executable_path=
      '/usr/local/Cellar/phantomjs211/bin/phantomjs',
      service_log_path='/tmp/ghostdriver.log')
else:
  print('Warning - Unknown OS:', sys.platform)
  print("Install PhantomJS")
  sys.exit()

url = 'https://www.mgm.gov.tr/?il=Istanbul'
browser.get(url)
html = browser.page_source

soup = bs4.BeautifulSoup(html, 'html.parser')

# Get day of the week
elems_day = soup.select('div.tahminTarih.ng-binding')

# Get city and district names in order to make sure query  
# returned correct results.
elems_il = soup.select('ziko.ng-binding')
# The weather forecasts at MGM's site is per city and district ("ilce")
# but many district names in Turkish  have non-ascii characters.
# Therefore, district-based queries not implemented.
# elems_ilce = soup.select('span.ng-binding')

  
# Get weather verbal
elems_tahmin = soup.select('div.tahminHadise.ng-binding')

# Reading of weather off of internat completed. Quit browser.
browser.quit()

# Check if the verbal weather forecast in Turkish includes words
# implying rain
umbrella = False
for keyword in rain_words:
  if elems_tahmin[0].getText().replace("I", "ı").replace("İ", "i").\
     lower().find(keyword) > 0:
    umbrella = True
    break
  
if umbrella:
  # Send email to yourself about the weather
  smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
  smtpObj.ehlo()
  smtpObj.starttls()

  from_addr = 'yyy@gmail.com'
  pswd = 'your_password' # getpass.getpass() not useful when run scheduled
  smtpObj.login(from_addr, pswd)

  to_addr = 'xxx@gmail.com'
  subject = 'Dışarı çıkarsan Şemsiye almayı unutma!'
  body_text = elems_day[0].getText() + '\n' + \
              elems_il[0].getText() + '\n' + \
              elems_tahmin[0].getText()
  body = ('\r\n').join([
              'From: %s' % from_addr,
              'To: %s' % to_addr,
              'Subject: %s' % subject ,
              '',
              body_text]
              )
  smtpObj.sendmail(from_addr, to_addr, body.encode('utf-8'))

  # log out of email server
  smtpObj.quit()
