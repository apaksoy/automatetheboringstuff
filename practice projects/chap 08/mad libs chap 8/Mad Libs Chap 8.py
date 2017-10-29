#!/usr/bin/env python3
'''
This program reads the text in "demlibsin.txt" file and replaces 
the ADJECTIVE, NOUN, ADVERB, or VERB words literally with the words
specified by the user. It prints out the new sentence to the screen
and to the "demlibs.out" file.
'''
'''
Create a Mad Libs program that reads in text files and lets the user
add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.

The results should be printed to the screen and saved to a new text
file.
'''

import re

# Open the file
dlFile = open('demlibsin.txt', 'r') # file should have already been
                                    # created 
dlString =dlFile.read()
dlFile.close

while True:
    # Find an occurence
    kwRegex = re.compile(r'(\s)(ADJECTIVE|NOUN|ADVERB|VERB)')
    found = kwRegex.search(dlString)
    if found: 
        # Ask for a replacement
        article = 'a'
        if found.group(2).lower() == 'adjective':
            article ='an'            
        newWord = input('Enter ' + article +' ' + found.group(2).lower() + ':\n')
        # Replace the word
        dlString = kwRegex.sub(r'\1' + newWord, dlString, count = 1)
    else:
        break

# Print the outcome to the screen
print(dlString)

# Print the outcome to a text file.
dlFile = open('demlibsout.txt', 'w')
dlFile.write(dlString)
dlFile.close()
