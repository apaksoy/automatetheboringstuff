#!/usr/bin/env python3
#  This program copies all specified types of files under a specified
#  folder to a new folder
'''
Write a program that walks through a folder tree and searches for files
with a certain file extension (such as .pdf or .jpg). Copy these files
from whatever location they are in to a new folder.
'''

import os
import re
import shutil
import sys

fileTypes = ('jpg', 'pdf')

# Confirm the existence and get the absolute path of the source
# and target folders

sourceFolder = './source'
sourceFolder = os.path.abspath(sourceFolder)
# folder name only, to print out
simpleSourceFolder = re.search(r'/([\w .-]+)$', sourceFolder).group(1)

targetFolder = './target'
targetFolder = os.path.abspath(targetFolder)
# folder name only, to print out 
simpleTargetFolder = re.search(r'/([\w .-]+)$',targetFolder).group(1) 

# Tell user the program has started and what it will be doing
if os.path.exists(sourceFolder):
    print('Will copy file types:\n')
    for fileType in fileTypes:
        print('%s' % (fileType))
    print('\nin "%s" folder \n' % (simpleSourceFolder))
else:
    print('Source folder %s does not exist.' % (sourceFolder))
    sys.exit()

if os.path.exists(targetFolder):
    print('\nto target folder "%s" \n' % (simpleTargetFolder))
else:
    print('Target folder %s does not exist.' % (targetFolder))
    sys.exit()

# Loop through the directory and its subdirectories
# to locate the specified types of files
# and paste them to the target directory
count = 0
for foldername, subfolders, filenames in os.walk(sourceFolder):
    print('\nCopying specified file types in "%s"...' % (os.path.basename(foldername)))
    for filename in filenames:
        for fileType in fileTypes:
            if filename.endswith('.' + fileType):
                # print('%s\nto\n%s' % (os.path.join(foldername, filename) , targetFolder)) # dry run
                print(shutil.copy(os.path.join(foldername, filename), targetFolder))
                count += 1

print('\nDone. %s files copied.' %(count))
