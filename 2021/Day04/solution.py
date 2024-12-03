from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().split("\n\n")
  data = [row.replace("\n", " ").replace("  ", " ") for row in data]  

board_side=5
inputs = data[0].split(",")
boards = data[1:]

def HasWon(grid):
  # Checks rows if all chars are the same = true
  for x in range(0, len(grid), board_side):
    if len(set(grid[x:x+board_side])) == 1:
      return True
  # Check columns
  for i in range(board_side):
    str = ""
    for j in range(i, len(grid), board_side):
      str += grid[j]
    if str == 'xxxxx':
      return True
  return False

def CountSum(grid):
  sum = 0
  for i in grid:
    if i == 'x':
      pass
    else:
      sum += int(i)      
  return sum

def getBoardGrids():
  boardGrids = list([])
  for _,v in enumerate(boards):    
    nums = v.strip().split(" ")            
    boardGrids.append(nums)
  return boardGrids

def findWinner(inputs, grids):
  for val in inputs:
    for grid in grids:
      if val in grid:  
        i = grid.index(val)              
        grid[i] = 'x'      
        if HasWon(grid):          
          return grid, int(val)
  return -1

def part1(inputs):
  grids = getBoardGrids()
  grid, lastvalue = findWinner(inputs, grids)
  return CountSum(grid) * lastvalue

def part2(inputs):          
  grids = getBoardGrids()
  num_grids = len(grids)
  winners = 0
  while(len(grids)>0):    
    grid, lastvalue = findWinner(inputs, grids)
    inputs = inputs[inputs.index(str(lastvalue)):]
    grids.remove(grid)
    winners += 1
    if winners == num_grids:
      return CountSum(grid) * lastvalue    
  return -1
  
print(part1(inputs))  
print(part2(inputs)) 