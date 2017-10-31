#!/usr/bin/env python3
'''
This program finds all the files with a given prefix
in a specified folder and locates any gaps in numbering
such as spam003.txt in spam001.txt, spam002.txt and
spam004.txt. It then renames all the latter files to fill
the gap.
'''
'''
Write a program that finds all files with a given prefix, such as
spam001.txt, spam002.txt, and so on, in a single folder and locates
any gaps in the numbering (such as if there is a spam001.txt and
spam003.txt but no spam002.txt). Have the program rename all the later
files to close this gap.
'''

import os
import re
import shutil
import sys

sourceFolder = './source'
sourceFolder = os.path.abspath(sourceFolder)
# simpleSourceFolder = re.search(r'/([\w .-]+)$',sourceFolder).group(1)

startStr = 'spam'

# Confirm existence of specified folder
if os.path.exists(sourceFolder):
    # Print a "welcome" message
    print('\nWill scan files starting with "{0}" for gaps in numbering in folder:'.format(startStr))
    print(sourceFolder, '\n')
else:
    print('Folder %s does not exist.' % (sourceFolder))
    sys.exit()

# Get the names of the files with the specified prefix
fileList = os.listdir(sourceFolder)

pattern = r'spam(\d*)\.txt'
orSerList = [] # original serial numbers

allFileCount = 0
for filename in fileList:
    mo = re.search(pattern, filename)
    if mo:
        allFileCount += 1
        orSerList.append(mo.group(1))

# Find the gap in numbering
orSerList.sort()

serialDict = {} # dictionary mapping original serial numbers
                # to new serial numbers
count = 0
for serialNo in orSerList:
    count += 1
    serialDict[serialNo] = str(count).zfill(3)

    
# Rename all the files after the gap
reCount = 0 # counter for number of files renamed
for key, value in serialDict.items():
    if key != value:
        reCount += 1
        oldFilename = 'spam' + key + '.txt'
        newFilename = 'spam' + value + '.txt'
        oldFilePath = os.path.join(sourceFolder, oldFilename)
        newFilePath = os.path.join(sourceFolder, newFilename)
        # change file name from new to old
        print('renaming {0} as {1}'.format(oldFilename,newFilename))
        shutil.move(oldFilePath, newFilePath)
        
print('{0} files renamed out of {1}.'.format(reCount, allFileCount))
