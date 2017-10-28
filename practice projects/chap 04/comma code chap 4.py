#!/usr/bin/env python3

'''
Write a function that takes a list value as an argument and
returns a string with all the items separated by a comma and
a space, with and inserted before the last item. For example,
passing the previous spam list to the function would return
'apples, bananas, tofu, and cats'. But your function should
be able to work with any list value passed to it.
'''

spam1 = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 1, 'tofu', 'cats']
spam3 = ['apples', 1, 'tofu', 'grapefruit', 2.0]

# returns a list in string while adding a comma in between every item 
# in oxford style and an "and" before the last item
def add_and(spam): 
    added = ''
    listLength = len(spam)

    for i in range(listLength):
        added += str(spam[i]) # add item to the string
        if i < (listLength - 1):
            added += ', '
        if i == (listLength - 2):
            added += 'and '

    return added

andAdded = add_and(spam3) 
print(andAdded)
    
