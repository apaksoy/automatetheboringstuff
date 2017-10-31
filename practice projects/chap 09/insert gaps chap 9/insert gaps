#!/usr/bin/env python3
'''
This program finds all the files with a given prefix and serial numbers
in a specified folder and renames them by changing theirserial numbers
so that files with in between serial numbers can be placed in. For example
it renames, spam004.txt as spam005.txt and spam003.txt as spam004.txt so
that a new file with the name spam003.txt can be insterted in.
'''
'''
As an added challenge, write another program that can insert gaps into
numbered files so that a new file can be added.
'''

import os
import re
import shutil
import sys


def insertGap(stList):
    ''' Finds the smallest gap in integer values of a series of numbers in
        strings and increases the values of all strings by 1 smaller than
        the gap. All values are raised by 1 if there are no gaps. The series
        is assumed to be already sorted in increasing order '''
    
    # convert string list to integer list
    i = 0
    list = []
    for i in range(len(stList)):
        list.append(int(stList[i]))

    print('list in function: ', list)
    
    number = list[0] + 1
    N = len(list)
    if N < 999 - (list[0] - 1): # check if there is at least one empty spot
        for i in range(1, N): # check if the end of list is reached
            if number < list[i]: # check if spot is empty
                i = i - 1 # i reduced by 1 as i + 1 is later used as number of
                          # items to be increased eventually
                break
            else:
                number += 1
                continue
        
        print('i:', i)
        # increase as many items in the list as necessary
        # Using i + 1 because because indexing for lists start from zero
        # unlike counting
        for j in range(i + 1):
            list[j] = list[j] + 1
            
        # convert integer list back to string
        i = 0
        stList = []
        for i in range(N):
            stList.append(str(list[i]).zfill(3))
    else: # there are no empty spots
        list = False 
    
    return stList





if __name__ == "__main__":
    # Confirm existence of the specified folder
    sourceFolder = './source'
    
    ''' # for Mac OS only
    sourceFolder = '/Users/Alper/Library/Mobile Documents/com~apple~CloudDocs' + \
                    '/Documents/Python/Automate the boring stuff/code/insert ' + \
                    'new files chap 9'
    '''
    
    sourceFolder = os.path.abspath(sourceFolder)
    # simpleSourceFolder = re.search(r'/([\w .-]+)$',sourceFolder).group(1)

    startStr = 'spam'
    insList = ['001', '003'] # serial numbers to be inserted
    print('insList: ', insList)

    # Confirm existence of specified directory
    if os.path.exists(sourceFolder):
        # Print a "welcome" message
        print('\nWill scan files starting with ' + startStr + \
              ' for gaps in numbering in folder:')
        print(sourceFolder, '\n')
    else:
        print('Folder %s does not exist.' % (sourceFolder))
        sys.exit()

    # Get the names of the files with the specified prefix
    fileList = os.listdir(sourceFolder)

    pattern = r'spam(\d*)\.txt'
    orSerList = [] # original file serial numbers

    allFileCount = 0
    for filename in fileList:
        mo = re.search(pattern, filename)
        if mo:
            allFileCount += 1
            orSerList.append(mo.group(1))
    serList = orSerList.copy() # this is the list to be manipulated
    serList.sort()


    # Initiate mapping of series with existing serial numbers.
    # This was done to have easier to understand code and to be able to reuse
    # previously written code.
    # If speed were an issue, this program could be written
    # without a dictionary.
    print('serList:', serList)
    serialDict = {}
    for serialNo in serList:
        serialDict[serialNo] = serialNo

    # Find the new serial numbers
    # insList is not updated at all during the modification of serial numbers
    # because once a gap is opened, the next intersection set automatically
    # no longer includes the insertion for which the gap was created.
    # The updating of the intersection set every time an insertion necessity is
    # tested and starting of modification from the smallest insertion in the set
    # guarantees gaps for all insertions
    for serial in insList:   
        # Find if to be inserted filenames already exist
        intSerList = list(set(serList) & set(insList))
        if intSerList == []: # get out of the loop as an insertion no longer needed
            break
        # Insert a gap in the serial numbers only for those new numbers
        # for which there are no gaps.
        smallest = min(intSerList)
        position = serList.index(smallest)
        tempList = serList[position:]

        print('\nbefore tempList:', tempList)
        tempList = insertGap(tempList)
        print('after tempList:', tempList)
        serList = serList[:position] + tempList
        print('updated serList:', serList)

    i = 0
    for key in serialDict:
        serialDict[key] = serList[i]
        i += 1
    print('updated serialDict', serialDict)
     
    # Rename all the files after the gap
    reCount = 0 # counter for number of files renamed
    # using reverse not to destroy any files while moving them around
    for key in reversed(list(serialDict.keys())):
        if key != serialDict[key]: # rename only if there is a change
            reCount += 1
            oldFilename = 'spam' + key + '.txt'
            newFilename = 'spam' + serialDict[key] + '.txt'
            oldFilePath = os.path.join(sourceFolder, oldFilename)
            newFilePath = os.path.join(sourceFolder, newFilename)
            # change file name from new to old
            print('renaming {0} as {1}'.format(oldFilename,newFilename)) # dry run
            shutil.move(oldFilePath, newFilePath)
            
    print('{0} files renamed out of {1}.'.format(reCount, len(serialDict)))
