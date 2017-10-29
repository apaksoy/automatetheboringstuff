#!/usr/bin/env python3
'''
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that
is at least eight characters long, contains both uppercase and lowercase
characters, and has at least one digit. You may need to test the string
against multiple regex patterns to validate its strength.
'''

import re

pw = 'snka1AB'

criteriaDict = {}
criteriaDict[r'(.){8,}'] = 'Password should be at least 8 characters long.'
criteriaDict[r'[A-Z]+'] = 'Password must have at least one UPPERCASE letter.'
criteriaDict[r'[a-z]+'] = 'Password must have at least one lowercase letter.'
criteriaDict[r'[0-9]+'] = 'Password must have at least one numeric digit.'

strength = True
for criterion in criteriaDict.keys():
    if not re.search(criterion,pw):
        print(criteriaDict[criterion])
        strength = False

if strength:
    print('Strong password: ', pw)
else:
    print('Weak password: ', pw)



""" for regex list implementation
regexList = []
regexList.append(re.compile(r'(.){8,}'))
regexList.append(re.compile(r'[A-Z]+'))
regexList.append(re.compile(r'[a-z]+'))
regexList.append(re.compile(r'[0-9]+')) """


""" for regex dictionary implementation
regexDict = {}
regexDict[re.compile(r'(.){8,}')] = 'Password should be at least 8 characters long.'
regexDict[re.compile(r'[A-Z]+')] = 'Password must have at least one UPPERCASE letter.'
regexDict[re.compile(r'[a-z]+')] = 'Password must have at least one lowercase letter.'
regexDict[re.compile(r'[0-9]+')] = 'Password must have at least one numeric digit.' """

    
""" for regex list implementation
strength = True
for pRegex in regexList:
    try:
        pRegex.search(pw).group()
    except AttributeError:
        print(pRegex)
        strength = False

if strength:
    print('Strong password: ', pw)
else:
    print('Weak password: ', pw)  """

""" for regex dictionary implementation
strength = True
for pRegex in regexDict.keys():
    try:
        pRegex.search(pw).group()
    except AttributeError:
        print(regexDict[pRegex])
        strength = False

if strength:
    print('Strong password: ', pw)
else:
    print('Weak password: ', pw)"""
