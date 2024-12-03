from os.path import abspath, dirname, join
import copy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()  
  data = [list(row) for row in data]  

def part1(data, dump):
  grid = Grid(matrix=data)
  start = grid.node(0, 0)
  width = len(data[0])-1
  height = len(data)-1
  end = grid.node(width, height)

  finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
  path, _ = finder.find_path(start, end, grid)  

  if dump:
    print(grid.grid_str(path=path, start=start, end=end))

  val = sum([int(data[i[1]][i[0]]) for i in path[1:]])
  #[print(int(data[i[1]][i[0]])) for i in path[1:]]
  return val

def part2(data):
  d = copy.deepcopy(data)  
  # Horizontal
  for _ in range(4):      
    for x, row in enumerate(d):      
      for y, val in enumerate(row):
        val = int(val)
        val = 1 if val == 9 else val+1
        d[x][y] = str(val) 
      data[x] += d[x]        

  #Vertical
  d = copy.deepcopy(data)   
  for _ in range(4):
    d = copy.deepcopy(d)
    for x, row in enumerate(d):   
      for y, val in enumerate(row):
        val = int(val)
        val = 1 if val == 9 else val+1
        d[x][y] = str(val)     
    for row in d:          
      data.append(row)                
  
  return part1(data, False)  

print(part1(data, False)) 
print(part2(data))