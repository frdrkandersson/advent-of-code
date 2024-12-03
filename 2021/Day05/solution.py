from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()  

def populateGrid(data, diagonal):
  d = defaultdict(int)  
  for seg in data:
    f,t = seg.split(" -> ")
    x1,y1 = f.split(",")
    x2,y2 = t.split(",")
    x1,x2,y1,y2 = int(x1),int(x2),int(y1),int(y2)    
    if x1==x2:      
      for y in range(min(y1,y2), max(y1+1,y2+1)):              
        d[f"{x1},{y}"] += 1 
    elif y1==y2:
      for x in range(min(x1,x2), max(x1+1,x2+1)):      
        d[f"{x},{y1}"] += 1 
    elif diagonal:      
      dx, dy = x2-x1, y2-y1
      d[f"{x1},{y1}"] += 1
      while True:
        if dx > 0:
          x1 += 1
        else:
          x1 -= 1
        if dy > 0:
          y1 += 1
        else:
          y1 -= 1
        d[f"{x1},{y1}"] += 1
        if (x1==x2 and y1==y2):          
          break                       
  return d

def getSum(grid, value):
  counter = 0
  for val in grid.values():
    if val >= value:
      counter += 1
  return counter

def part1(data):    
  grid = populateGrid(data, False)  
  return getSum(grid, 2)

def part2(data):          
  grid = populateGrid(data, True)  
  return getSum(grid, 2)

print(part1(data))  
print(part2(data)) 