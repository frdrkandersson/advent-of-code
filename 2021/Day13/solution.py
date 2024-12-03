from os.path import abspath, dirname, join
import copy

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:  
  data = f.read().split("\n\n")
  data = [row.split("\n") for row in data]    
  coordinates = [row.split(",") for row in data[0]]  
  folds = [row.replace("fold along ", "").split("=") for row in data[1]]  

def dump(sheet):  
  width = 0
  height = 0
  for p in sheet:
    width = max(width, int(p[0]))
    height = max(height, int(p[1]))  

  for y in range(height+1):
    print()
    for x in range(width+1):
      if [str(x), str(y)] in sheet:
        print("#", end='') 
      else:
        print(".", end='')
  print()
    


def fold(arr1, arr2, splitpos, vertical):    
  for pos in arr2:
    if vertical:
      newX = splitpos - int(pos[0])
      newPos = [str(newX), pos[1]]
    else:            
      newY = splitpos - int(pos[1])
      newPos = [pos[0], str(newY)]

    if newPos not in arr1:
      arr1.append(newPos)      
  return arr1

def startFolding(sheet, folds):
  for line in folds:    
    tmpSheet = sheet.copy()    
    if line[0] == "y":
      newSheet = []
      y = int(line[1])
      for pos in sheet:        
        splitPos = int(pos[1])
        if splitPos == y:
          sheet.remove(pos)
        elif splitPos > y:          
          tmpSheet.remove(pos)
          pos[1] = str(splitPos-y)
          newSheet.append(pos)                
      fold(tmpSheet, newSheet, y, False)
    elif line[0] == "x":
      newSheet = []      
      x = int(line[1])
      for pos in sheet:        
        splitPos = int(pos[0])
        if splitPos == x:
          sheet.remove(pos)
        elif splitPos > x:
          pos[0] = str(splitPos-x)          
          newSheet.append(pos)
          tmpSheet.remove(pos)            
      fold(tmpSheet, newSheet, x, True)
    sheet = tmpSheet.copy()
  return sheet

def part1(sheet, folds):    
  return len(startFolding(sheet, folds))

def part2(sheet):
  dump(startFolding(sheet, folds))  

print(part1(copy.deepcopy(coordinates), [folds[0]])) 
part2(copy.deepcopy(coordinates))