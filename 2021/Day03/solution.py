from os.path import abspath, dirname, join
from collections import defaultdict
from bitarray import bitarray
from bitarray.util import ba2int

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

bitlength = len(data[0])

def parseInput(data) -> defaultdict(int):
    d = defaultdict(int)
    for _,val in enumerate(data):      
      for i in range(bitlength):
        d[i] += int(val[i])
    return d

def part1(data):      
  d = parseInput(data)
  str = ""
  for k,v in d.items():
    if v > len(data) / 2:
      str += "1"
    else:
      str += "0"  
  ba = bitarray(str)  
  return ba2int(ba) * ba2int(~ba)  

def part2(data):        
  dOxygen = parseInput(data)
  dco2 = parseInput(data)
  oxygen = data
  co2 = data  
  for i in range(bitlength):
    if len(oxygen) > 1:
      if dOxygen[i] >= len(oxygen) / 2:
          oxygen = list(filter(lambda x: x[i] == "1", oxygen))
      else:      
          oxygen = list(filter(lambda x: x[i] == "0", oxygen))
      dOxygen = parseInput(oxygen)

  for i in range(bitlength):
    if len(co2) > 1:
      if dco2[i] >= len(co2) / 2:  
          co2 = list(filter(lambda x: x[i] == "0", co2))
      else:
          co2 = list(filter(lambda x: x[i] == "1", co2))   
      dco2 = parseInput(co2)

  baOxygen = bitarray(oxygen[0])
  baco2 = bitarray(co2[0])  
  return ba2int(baOxygen) * ba2int(baco2)

print(part1(data))  
print(part2(data)) 