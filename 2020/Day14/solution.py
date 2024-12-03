from os.path import abspath, dirname, join 
from functools import reduce

with open(abspath(join(dirname(__file__), 'x.txt')), 'r') as f:  
  data = f.read().splitlines()  
  data = [row.replace(" ", "") for row in data]

def part1(data):    
  mask = ""  
  for row in data:
    key, value = row.split("=")       
    if key == "mask":
      mask = value
      print(mask)
    else:
      result = ""
      bits = f'{int(value):036b}'
      for i, c in enumerate(mask):        
        if c == "X":
          result += bits[i]
        if c != "X":
          result += c               
      b = str.encode(result)          
      #b = bytearray(result, "utf-8")
      print(int(b))
  
print(part1(data))
#print(part2(data))