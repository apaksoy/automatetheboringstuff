#!/usr/bin/env python3
'''
Write a function that takes a string and does the same thing as
the strip() string method. If no other arguments are passed other
than the string to strip, then whitespace characters will be removed
from the beginning and end of the string. Otherwise, the characters
specified in the second argument to the function will be removed from
the string.
'''

import re

# simulation of string data type's strip() method
def astrip(string, character):
    if character:
        # strip character from ends
        bcRegex = re.compile(r'^'+character+r'*')
        ecRegex = re.compile(character+r'*$')
        string = bcRegex.sub(r'',string)
        string = ecRegex.sub(r'',string)
    else:
        # strip white space from ends
        bwsRegex = re.compile(r'^\s*')
        ewsRegex = re.compile(r'\s*$')
        string = bwsRegex.sub(r'',string)
        string = ewsRegex.sub(r'',string)
    return string

string = 'aaterkosaa'
print('original string:', string)
string = astrip(string,'a')
print('modified string:', '*' + string + '*')
