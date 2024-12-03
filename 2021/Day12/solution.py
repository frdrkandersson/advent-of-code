from os.path import abspath, dirname, join
from collections import Counter

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()
  data = [i.split("-") for i in data]

def twiceInDict(d):
  for k, v in d.items():
    if k.islower() and v >= 2 and v != "end":
      return True
  return False  

def findNextStep(data, paths, result, twice):
  if len(paths) == 0:
    return

  newPaths = []
  for path in paths:  
    find = path[-1]
    for pair in data:
      if pair[0] == find and pair[1] != find:      
        if pair[1].islower():
          if twice:            
            if twiceInDict(Counter(path)) and pair[1] in path:
              continue
          elif pair[1] in path:
            continue

        newPath = path.copy()
        newPath.append(pair[1])
        if pair[1] == "end":
          result.append(newPath)
        else:
          newPaths.append(newPath)        
      elif pair[1] == find and pair[0] != find:
        if pair[0].islower():                     
          if twice:            
            if twiceInDict(Counter(path)) and pair[0] in path:
              continue
          elif pair[0] in path:
            continue

        newPath = path.copy()
        newPath.append(pair[0])
        if pair[0] == "end":
          result.append(newPath)
        else:
          newPaths.append(newPath)

  findNextStep(data, newPaths, result, twice)

def part1(data, twice):  
  paths = []  
  for pair in data.copy():
    if pair[0] == "start":
      paths.append(["start", pair[1]])  
      data.remove(pair)      
    elif pair[1] == "start":      
      paths.append(["start", pair[0]])          
      data.remove(pair)
  
  result = []
  findNextStep(data, paths, result, twice)   
  return len(result)

def part2(data):  
  return part1(data, True)

print(part1(data.copy(), False)) 
print(part2(data.copy()))