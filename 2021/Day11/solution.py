from os.path import abspath, dirname, join
import copy

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()
  data = [list(row) for row in data]
  for y in range(len(data)):
    for x in range(len(data[0])):
      data[x][y] = int(data[x][y])  

def bump(grid, x, y, flashed):
  try:
    grid[x][y] += 1
  except:
    return
  
  if grid[x][y] > 9:
    grid[x][y] = 0    
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0 or (x+i == -1 or y+j == -1):
          pass
        else:                    
          bump(grid, x+i, y+j, flashed)
    flashed.append((x,y))      
  return  

def step(grid):
  flashed = []
  for y in range(len(grid)):
    for x in range(len(grid[0])):      
      bump(grid, x, y, flashed)
      for i in flashed:
        grid[i[0]][i[1]] = 0    
  return len(flashed)

def part1(grid):
  return sum([step(grid) for _ in range(195)])
  
def part2(grid):
  flashes = 0
  counter = 0  
  while flashes < len(grid) * len(grid[0]):
    flashes = step(grid)
    counter += 1  
  return counter  

print(part1(copy.deepcopy(data))) 
print(part2(copy.deepcopy(data)))