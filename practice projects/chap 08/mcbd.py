#! python3 
'''
mcbd.py - Saves and loads pieces of text from/to the clipboard to/from a
          shelf type file.
Usage: python3 mcbd.py save <keyword> - saves clipboard for keyword.
       python3 mcbd.py <keyword> - loads to clipboard for keyword.
       python3 mcbd.py list - loads all keywords to clipboard.
       python3 mcbd.py delete <keyword> - deletes for keyword.
       python3 mcbd.py delete - deletes all keywords.
'''
'''
Say you have the boring task of filling out many forms in a web page or
software with several text fields. The clipboard saves you from typing
the same text over and over again. But only one thing can be on the
clipboard at a time. If you have several different pieces of text that
you need to copy and paste, you have to keep highlighting and copying
the same few things over and over again. You can write a Python
program to keep track of multiple pieces of text.
'''
'''
Extend the multiclipboard program in this chapter so that it has a
delete <keyword> command line argument that will delete a keyword from
the shelf. Then add a delete command line argument that will delete all
keywords.
'''

import pyperclip
import shelve
import sys
import textwrap

def print_usage():
    print(textwrap.dedent(
        '''
        Usage: python3 mcbd.py save <keyword> - saves clipboard for keyword.
               python3 mcbd.py <keyword> - loads to clipboard for keyword.
               python3 mcbd.py list - loads all keywords to clipboard.
               python3 mcbd.py delete <keyword> - deletes for keyword.
               python3 mcbd.py delete - deletes all keywords.
        '''))

mcbShelf = shelve.open('mcb')

# save or delete specified keywords
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print('clipboard saved under keyword:', sys.argv[2])
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
        print('deleted keyword:', sys.argv[2])
# list or delete all keywords or fetch one
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print('all keywords copied to clipboard')
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('all keywords deleted')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print('copied to clipboard for keyword:', sys.argv[1])
    else:
        print('no such keyword:', sys.argv[1])
        print_usage()
else:
    print_usage()


mcbShelf.close()



