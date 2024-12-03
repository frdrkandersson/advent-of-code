from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().split(",")

data_ints = [int(i) for i in data]

def part1(data: list[int], days: int) -> int:      
  fishes = data[:]  
  dayCounter = 0
  while(True):    
    newFishes = 0
    for i,_ in enumerate(fishes):
      fishes[i] -= 1
      if fishes[i] == -1:
        fishes[i] = 6
        newFishes += 1       

    [fishes.append(8) for _ in range(newFishes)]         

    dayCounter += 1    
    if dayCounter == days:
      break

  return len(fishes)

def part2(data, days):     
  # Instead keep track of how many fishes breed upcoming 9 days
  d = defaultdict(int)
  for i in range(9):
    d[i] = 0  

  for fish in data:
      d[fish] += 1  
  
  for _ in range(days):
    d2 = defaultdict(int)
    for k,v in sorted(d.items()):
      if k == 0:
        d2[6] += v
        d2[8] += v
      else:
        d2[k-1] += v 
    d=d2
  return sum(d.values())    

print(part1(data_ints, 80))  
print(part2(data_ints, 256))