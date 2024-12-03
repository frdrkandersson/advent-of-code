from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().splitlines()  

pair = dict({')': '(', ']': '[', '}': '{', '>': '<'})
swappedPair = dict([(value, key) for key, value in pair.items()]) 

def parseRow(row, scoreTable, returnStack):
  stack = []
  for c in row:                 
    if c in pair.values():
      stack.append(c)
    elif len(stack) > 0 and pair[c] == stack[-1]:        
      stack.pop()
    else:      
      return [] if returnStack else scoreTable[c]      
  return stack if returnStack else 0

def part1(data):
  scoreTable = dict({')': 3, ']': 57, '}': 1197, '>': 25137})
  return sum([parseRow(row, scoreTable, False) for row in data])  
  
def part2(data):
  scoreTable = dict({')': 1, ']': 2, '}': 3, '>': 4})
  scores = []
  for row in data:
    stack = parseRow(row, scoreTable, True)        
    if stack != []:      
      s = 0
      for c in reversed(stack):      
        s = (s * 5) + scoreTable[swappedPair[c]]      
      scores.append(s)

  scores = sorted(scores)  
  middle = scores[(len(scores) - 1)//2]
  return middle

print(part1(data)) 
print(part2(data))