from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()
    
data_ints = [int(i) for i in data]

def part1(ints):  
  count = 0
  prev = 0
  for i in ints:    
    if i > prev and prev != 0:        
        count += 1
    prev = i
  return count

def part2(ints):    
  d = defaultdict(int)  
  for i, val in enumerate(ints):      
        d[i] += val
        if i-1 >= 0:
            d[i-1] += val
        if i-2 >= 0:
            d[i-2] += val        
  d.popitem()
  d.popitem()    
  return part1(list(d.values()))

print(part1(data_ints))  
print(part2(data_ints)) 