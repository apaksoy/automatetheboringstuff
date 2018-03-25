#!/usr/bin/env python3
''' Write a program that takes a list of people’s email addresses and a
list of chores that need to be done and randomly assigns chores to
people. Email each person their assigned chores. If you’re feeling
ambitious, keep a record of each person’s previously assigned chores so
that you can make sure the program avoids assigning anyone the same
chore they did last time. For another possible feature, schedule the
program to run once a week automatically.
'''

import random
import smtplib
import sys

# Get email addresses and chores
emails = [('Alper', 'www@gmail.com'),
          ('Alperus', 'xxx@gmail.com'),
          ('Jonathan','yyy@gmail.com'),
          ('Jerry', 'zzz@gmail.com')]
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

# quit program if no chores more than people
assert len(emails) >= len(chores),\
    f'Number of chores: {len(chores)} more than number'\
        f' of people {len(emails)}'

# Choose an email, assign it to a chore
assignments = []
for chore in chores:
    randomEmail = random.choice(emails)
    assignments.append((randomEmail+ (chore,)))
    emails.remove(randomEmail) # this email is now assigned, remove it

# Email the chore
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

from_addr = 'abcd@gmail.com'
password = input('Type password and press Enter: ')
try:
    smtpObj.login(from_addr, password)
except Exception as msg:
    print(f'There was a problem: {msg}')
    sys.exit()

for name, email, chore in assignments:
    to_addr = email
    subject = f'This week\'s assignment: {chore.upper()}'
    body_text = f'Hi {name},\n\n Can you pls do the {chore.upper()} this week? Thanks! \n\nAlper'
    body = ('\r\n').join([
                'From: %s' % from_addr,
                'To: %s' % to_addr,
                'Subject: %s' % subject ,
                '',
                body_text]
                )
    smtpObj.sendmail(from_addr, to_addr, body)

smtpObj.quit()

