#!/usr/bin/env python3
''' Using the os.walk() function from Chapter  9, write a script that
will go through every PDF in a folder (and its subfolders) and encrypt
the PDFs using a password provided on the command line.

Save each encrypted PDF with an _encrypted.pdf suffix added to the
original filename.

Before deleting the original file, have the program attempt to read
and decrypt the file to ensure that it was encrypted correctly.
'''

import os
import re
import sys
import PyPDF2
from send2trash import send2trash

fileType = 'pdf'
pwd = 'nelson'

sourceFolder = '.'
sourceFolder = os.path.abspath(sourceFolder)
# folder name only, to print out
simpleSourceFolder = re.search(r'/([\w .-]+)$', sourceFolder).group(1)

# Tell user the program has started and what it will be doing
if os.path.exists(sourceFolder):
    print(f'Encrypting PDF files in "{simpleSourceFolder}"'
          'and below \n')
else:
    print(f'Source folder "{simpleSourceFolder}" does not exist.')
    sys.exit()

# Loop through the directory and its subdirectories
# to find all pdf files
# Once located, encrypt each and every pdf file
# and test encryption
count = 0
for foldername, subfolders, filenames in os.walk(sourceFolder):
    for filename in filenames:
        if filename.endswith('.' + fileType):
            # get pages of source pdf and copy them to new pdf
            pdfReader = PyPDF2.PdfFileReader(
                    open(os.path.join(foldername, filename), 'rb'))
            # encrypt if not already encrypted
            if not pdfReader.isEncrypted:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(0, pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(pwd)  # apply encryption to pdf object
                # create file enclosure & merge with encrypted object
                newFilename = filename.rstrip('.' +
                        fileType) + '_e' + '.' + fileType
                resPdf = open(os.path.join(foldername, newFilename),
                        'wb')
                pdfWriter.write(resPdf)
                resPdf.close()  # close merged object

                # test encryption
                pdfReader = PyPDF2.\
                    PdfFileReader(open(os.path.join(
                    foldername, newFilename), 'rb'))
                if pdfReader.isEncrypted:
                    if pdfReader.decrypt(pwd) == 1:
                        print(f'{newFilename} now encyrpted')
                        # print(os.path.join(foldername, filename)
                        # + ' deleted') # dry run
                        send2trash(os.path.join(foldername, filename))
                        count += 1
                    else:
                        print(f'wrong password for '
                              f'{os.path.join(foldername,newFilename)}')
                else:
                    print(f'{os.path.join(foldername, filename)}'
                              f' could not be encrypted')
            else:
                print(f'{os.path.join(foldername, filename)}'
                          f' already encrypted')

print(f'\nDone. {count} files encrypted with password "{pwd}".')
