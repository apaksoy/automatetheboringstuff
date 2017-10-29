#!/usr/bin/env python3
'''
Write a function named printTable() that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your printTable() function would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

'''


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):

    # find maximum word length for each column
    colWidths = [0] * len(table)
    for i in range(len(table)): 
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])

    # print each column justified to the right
    innerLength = len(table[0])
    i = 0
    while i < innerLength: 
        for j in range(len(table)):
            print(table[j][i].rjust(colWidths[j]), end=' ')
        print('')
        i += 1

                           
printTable(tableData)
