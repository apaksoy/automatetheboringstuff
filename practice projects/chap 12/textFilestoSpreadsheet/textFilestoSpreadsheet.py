#!/usr/bin/env python3
'''
Write a program to read in the contents of several text files (you can
make the text files yourself) and insert those contents into a
spreadsheet, with one line of text per row. The lines of the first
text file will be in the cells of column A, the lines of the second
text file will be in the cells of column B, and so on.
'''

import openpyxl

fileNameList = ['TextOne.txt', 'TextTwo.txt', 'rj.txt']

wb = openpyxl.Workbook()
sheet = wb.active

# enumerate() provides an automatic counter to be used in excel cell
# referencing.
for fileCounter, name in enumerate(fileNameList):
    #some of my text files include characters with non-ASCII Unicodes 
    txtfileObj = open(name, encoding='utf-8') 
    lines = txtfileObj.readlines()
    for lineCounter, line in enumerate(lines):
        sheet.cell(row=lineCounter + 1, column=fileCounter + 1).value = line

wb.save('TexttoSpreadsheet.xlsx')
