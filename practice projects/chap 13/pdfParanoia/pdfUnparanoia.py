#!/usr/bin/env python3
'''write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided
password. If the password is incorrect, the program should print a
message to the user and continue to the next PDF.
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
    print(f'Decrypting PDF files in "{simpleSourceFolder}"'
          'and below \n')
else:
    print(f'Source folder "{simpleSourceFolder}" does not exist.')
    sys.exit()

# Loop through the directory and its subdirectories
# to find all PDF files.
# Once located, dectrypt PDF file to a new file and test if decprypted.
countDec = 0
countPdf = 0
for foldername, subfolders, filenames in os.walk(sourceFolder):
    for filename in filenames:
        if filename.endswith('.' + fileType):
            countPdf += 1
            # get pages of source pdf and copy them to new pdf
            pdfReader = PyPDF2.PdfFileReader(
            open(os.path.join(foldername, filename), 'rb'))
            # decrypt if encrypted
            if pdfReader.isEncrypted == 1:
                pdfReader.decrypt(pwd)  # decrpty pdf object
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(0, pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                # create file enclosure & merge with decrypted object
                newFilename = filename.rstrip('.' +
                        fileType) + '_d' + '.' + fileType
                resPdf = open(os.path.join(foldername, newFilename),
                        'wb')
                pdfWriter.write(resPdf)
                resPdf.close()  # close merged object

                # test decryption
                pdfReader = PyPDF2.PdfFileReader(open(os.path.join(
                        foldername, newFilename), 'rb'))
                if pdfReader.isEncrypted == 0:
                    print(f'{newFilename} now encyrpted')
                    countDec += 1
                else:
                    print(f'{os.path.join(foldername, filename)}'
                              f' can not be decrypted with password'
                              f' "{pwd}"')
            else:
                print(f'{os.path.join(foldername, filename)}'
                          f' already decrypted')

print(f'\nDone. {countDec} out of {countPdf} PDF files decrypted'
      f' with password "{pwd}".')
