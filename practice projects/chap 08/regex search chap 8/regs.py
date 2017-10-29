#!/usr/bin/env python3
'''
Searches text files in working directory for user supplied keywords
without case sensitivity
usage - python3 regs.py <regex>
'''
'''
Write a program that opens all .txt files in a folder and searches for
any line that matches a user-supplied regular expression. The results
should be printed to the screen.
'''

import os
import re
import sys

if len(sys.argv) < 2:
    print('usage: python3 regs.py <keyword>')
    sys.exit()
keyword = sys.argv[1]

# Get the names of the .txt files in the folder.
match = False
for fileName in os.listdir():
    # Open each text file.
    if re.search(r'\.txt$', fileName):
        textFile = open(fileName, 'r')
        # Search the file for user supplied regex.
        contentFile = textFile.readlines()
        for everyLine in contentFile:
            if re.search(keyword, everyLine, re.I):
                # Print any lines found matching the user supplied
                # regex.
                print('match from file', fileName + ':', everyLine.strip('\n'))
                match = True
        textFile.close()
        
if not match:
    print('no text files found containing keyword:', keyword)
