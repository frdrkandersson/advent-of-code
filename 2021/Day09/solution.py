from os.path import abspath, dirname, join
from functools import reduce
from typing import TypeVar

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()  

T = TypeVar("T")

def tryGet(T, x, y):
  if (x == -1 or y == -1):
    return 10

  try:
    return int(T[x][y])
  except:
    return 10

def part1(data: list[str]):
  sum = 0
  arr = []
  for row, i  in enumerate(data):
    for col, j  in enumerate(i):                  
      val = int(data[row][col])
      right = tryGet(data, row ,col+1)
      left = tryGet(data, row ,col-1)
      up = tryGet(data, row-1, col)
      down = tryGet(data, row+1, col)      
      if val < min(right, left, up, down):                  
        sum += val + 1
        arr.append([row,col])
  return sum, arr

def traverse(data, x, y, visited):    
  val = tryGet(data, x, y)
  if val >= 9:    
    return  

  if (x,y) in visited:
    return  
             
  visited[(x,y)] = True
  traverse(data, x+1, y, visited)
  traverse(data, x-1, y, visited)
  traverse(data, x, y+1, visited)
  traverse(data, x, y-1, visited)  
  return

def part2(data, points):  
  basins = []  
  for p in points:
    visited = {}  
    traverse(data, p[0], p[1], visited)
    basins.append(len(visited))

  basins.sort(reverse=True)          
  basins_product = reduce((lambda x, y: x * y), basins[:3])
  return basins_product

result, lowpoints = part1(data)
print(result) 
print(part2(data,lowpoints))