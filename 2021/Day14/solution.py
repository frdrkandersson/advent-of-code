from os.path import abspath, dirname, join
from collections import Counter

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().split("\n\n")
  data = [row.split("\n") for row in data]
  template = data[0][0]
  pair = dict([row.split(" -> ") for row in data[1]])

def run(template, pair, rounds):
  pairCounter = Counter()
  charCounter = Counter(template)

  for i in range(len(template)-1):
    p = template[i:i+2]
    pairCounter[p] += 1

  for _ in range(rounds):
    tempPairCounter = Counter()
    for k,v in pairCounter.items():
      if k in pair:        
        charCounter[pair[k]] += v
        tempPairCounter[k[0] + pair[k]] += v
        tempPairCounter[pair[k] + k[1]] += v                               
    pairCounter = tempPairCounter

  return max(charCounter.values()) - min(charCounter.values())     

def part1(template, pair):  
  return run(template, pair, 10)

def part2(template, pair):
  return run(template, pair, 40)        

print(part1(template, pair)) 
print(part2(template, pair))