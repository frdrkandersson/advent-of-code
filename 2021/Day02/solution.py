from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

def part1(data):    
  grid = [0, 0] 
  for str in data:    
    action, value = str.split()
    if action == "forward":
      grid[0] += int(value)
    elif action == "down":
      grid[1] += int(value)
    elif action == "up":    
      grid[1] -= int(value)
  return grid[0] * grid[1]

def part2(ints):    
  grid = [0, 0, 0] 
  for str in data:    
    action, value = str.split()
    if action == "forward":
      grid[0] += int(value)
      grid[1] += grid[2] * int(value)
    elif action == "down":
      grid[2] += int(value)
    elif action == "up":    
      grid[2] -= int(value)    
  return grid[0] * grid[1]

print(part1(data))  
print(part2(data)) 