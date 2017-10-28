#!/usr/bin/env python3
'''
Copy the previous grid value, and write code that
uses it to print the image.
'''

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

innerLength = len(grid[0])
i = 0
# repeat as many times as the number of secondary items in each inside list  
while i < innerLength:
    # repeat as many times as the number of primary items
    for j in range(len(grid)):           
        print(grid[j][i], end='')
    print('')
    i += 1
