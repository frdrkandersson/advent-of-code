import re
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

chars = ['X','M','A','S']
directions = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))

def traverse(data, x, y, direction, char_index):
    x, y = x+direction[0], y+direction[1]    
    
    if char_index >= len(chars):
        return 1

    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):        
        return 0

    if data[x][y] != chars[char_index]:
        return 0
    
    return traverse(data, x, y, direction, char_index+1)

def check_diagonals(data, x, y):
    try:
        top_left_bottom_right = (data[x-1][y-1] == 'M' and data[x+1][y+1] == 'S') or (data[x-1][y-1] == 'S' and data[x+1][y+1] == 'M')
        bottom_left_top_right = (data[x+1][y-1] == 'M' and data[x-1][y+1] == 'S') or (data[x+1][y-1] == 'S' and data[x-1][y+1] == 'M')
        if top_left_bottom_right and bottom_left_top_right:
            return 1        
    except:
        return 0   
    return 0

def part1(input):    
    result = 0

    for row, i  in enumerate(data):
        for col, _  in enumerate(i):
            if input[row][col] == chars[0]:                
                for direction in directions:                    
                    result += traverse(input, row, col, direction, 1)

    return result

def part2(input):
    result = 0

    for row, i  in enumerate(data):
        for col, _  in enumerate(i):
            if input[row][col] == 'A':
                result += check_diagonals(input, row, col)

    return result

print(part1(data))
print(part2(data))