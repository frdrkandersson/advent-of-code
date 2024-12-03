from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()
  data = [i.split(" | ") for i in data]

def part1(data):
  sum = 0
  for row in data:        
    for output in row[1].split(" "):
      if len(output) in [2,3,4,7]:
        sum += 1
  return sum

def mapNumbers(newValues):
  # Screen segment counting from top left to right starting at 0
  d = defaultdict()
  d[0] = {0,1,2,4,5,6}
  d[1] = {2,5}
  d[2] = {0,2,3,4,6}
  d[3] = {0,2,3,5,6}
  d[4] = {1,2,3,5}
  d[5] = {0,1,3,5,6}
  d[6] = {0,1,3,4,5,6}
  d[7] = {0,2,5}
  d[8] = {0,1,2,3,4,5,6}
  d[9] = {0,1,2,3,5,6}
  
  dNew = defaultdict()  
  for k,v in d.items():
    str = ""
    for x in v:
      str += newValues[x]  
    str = ''.join(sorted(str))
    dNew[str] = k

  return dNew

def contains(s1, s2):
  for i in s1:
    if i not in s2:
      return False
  return True 

def subtract(s1, s2):  
  for i in s1:    
    s2 = s2.replace(i, '')
  return s2

def intersect(s1, s2):
  s = ""
  for i in s1:
    if i in s2:
      s += i  
  return s

def part2(data):
  result = 0
  for row in data:
    num = defaultdict(list[str])
    d3 = defaultdict(str)
    signals = row[0].split(" ")    
    for signal in signals:
      num[len(signal)].append(signal)      
    
    one = num[2][0]
    seven = num[3][0]
    four = num[4][0]
    eight = num[7][0]
    
    d3[0] = subtract(one, seven)

    six = ""    
    nine = ""    
    for n in num[6]:      
      if not contains(one, n):        
        six = n
      elif len(subtract(n, four)) == 1:
        d3[3] = subtract(n, four)
      else:
        nine = n                     

    d3[5] = intersect(one, six)    
    d3[2] = subtract(six, eight)    
    d3[1] = subtract(d3[3], subtract(one,four))    
    d3[4] = subtract(nine, eight)

    d3[6] = eight
    for i in range(6):      
      d3[6] = subtract(d3[i], d3[6])
    
    newStrings = mapNumbers(d3)    

    outputValue = ""
    for output in row[1].split(" "):      
      output = ''.join(sorted(output))
      outputValue += str(newStrings[output])
    
    result += int(outputValue)
  return result

print(part1(data)) 
print(part2(data))