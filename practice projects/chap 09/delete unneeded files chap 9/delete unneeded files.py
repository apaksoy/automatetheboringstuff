#!/usr/bin/env python3
#  This program finds files that are above a specified size within
#  a specified folder and its subfolders
'''
Write a program that walks through a folder tree and searches for
exceptionally large files or folders—say, ones that have a file size of
more than 100MB. (Remember, to get a file’s size, you can use
os.path.getsize() from the os module.) Print these files with their
absolute path to the screen.
'''

import os
import shutil
import sys

# converts byte to megabytes
def mb (size):
    return size / (1024 * 1024)

# Confirm existence of the specified folder
sourceFolder = './source'
sourceFolder = os.path.abspath(sourceFolder)
# simpleSourceFolder = re.search(r'/([\w .-]+)$',sourceFolder).group(1)

tSize = 0.5 * 1024 * 1024 # 0.5 MB

if os.path.exists(sourceFolder):
    print('\nWill scan for files with more than {0:.2} MB in size in'.\
          format(mb(tSize)))
    print(sourceFolder)
else:
    print('Source folder %s does not exist.' % (sourceFolder))
    sys.exit()


count = 0        # number of files scanned
countAbove = 0   # number of files found above the threshold
size = 0         # number of files 
sizeAbove = 0    # total size of files found in MB

# Walk through the specified folder
# while finding the locations of files above a certain size
# and printing out their paths.
for foldername, subfolders, filenames in os.walk(sourceFolder):
    print('\nExamining "{0}" for large files...'.\
          format(os.path.basename(foldername)))
    for filename in filenames:
        count += 1
        fileSize = os.path.getsize(os.path.join(foldername, filename))
        size += fileSize
        if fileSize >= tSize:
            print('Found: "{0}", {1:.2} MB'.format(filename,\
                                                mb(fileSize)))
            countAbove += 1
            sizeAbove += fileSize


print('\nReviewed {0} files with'\
      ' a total size of {1:,} MB.'.format(count,\
int(mb(size))))

print('Found {0} of them to be above {1:.2} MB '\
      'with a total size of {2} MB.'.\
format(countAbove, tSize / (1024 * 1024), int(mb(sizeAbove))))
