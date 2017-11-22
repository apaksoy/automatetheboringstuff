#!/usr/bin/env python3
'''Say you have an encrypted PDF that you have forgotten the password
to, but you remember it was a single English word. Trying to guess your
forgotten password is quite a boring task. Instead you can write a
program that will decrypt the PDF by trying every possible English word
until it finds one that works. This is called a brute-force password
attack.
'''
''' I have completed this assignment as requested but note that PyPDF2
is hardly a universal decrypter for PDF files. There are many PDF
encryption algorithms it can not decrypt. See
https://github.com/mstamy2/PyPDF2/issues/378
for further details.

Warning: I have a relatively old computer. This program took nearly
25 minutes to succesffuly decrypt the menitoned the specified file.  
'''

import PyPDF2

# Get the dictionary file
dictFile = open('dictionary.txt', 'r')
wordsStr = dictFile.read()
wordsLst = wordsStr.split('\n')

# Get the specified PDF file
pdfFilename = 'test file one_e.pdf'
pdfFileObj = open(pdfFilename, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
if pdfReader.isEncrypted == 1:
    # Loop over the words in dictionary until the PDF file encrypted
    for word in wordsLst:
        # if decrypted, copy contents to new unencrypted PDF file
        if pdfReader.decrypt(word.upper()) or\
                pdfReader.decrypt(word.lower()):
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(0, pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            # create file enclosure & merge with decrypted object
            newPdfFilename = pdfFilename.rstrip('.pdf') + '_d' + '.pdf'
            resPdf = open(newPdfFilename, 'wb')
            pdfWriter.write(resPdf)
            resPdf.close()  # close merged object
            pdfFileObj.close()
            print(f'"{pdfFilename}" is decrypted via the password '
                    f'"{word}" and saved as "{newPdfFilename}"')
            break
    else:
        pdfFileObj.close()
        print(f'{pdfFilename} could not be decrypted')
