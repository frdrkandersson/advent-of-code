from os.path import abspath, dirname, join
import copy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read() 

hex = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111'
}

def hexaToBits(hexa):
  str = ""
  for c in hexa:    
    str += hex[c]
  return str

def binToDec(s): return int(s, 2)

def literal(index, version):  
  s = ""
  bits = '1'
  while bits[0] == '1':
    bits = data[index:index+5]    
    s += data[index+1:index+5]
    index += 5
  return version, index

def operator15(index, sumVerNr):   
  totalLength = binToDec(data[index+1:index+16])  
  i = 0
  index += 16
  while i < totalLength:            
    ver, newindex = run(index)
    sumVerNr += ver
    i += (newindex-index)    
    index = newindex
  return sumVerNr, index   

def operator11(index, sumVerNr):    
  numberOfSubs = binToDec(data[index+1:index+12])  
  index += 12
  for _ in range(numberOfSubs):  
    ver, index = run(index)
    sumVerNr += ver    
  return sumVerNr, index

def sum(index, sumVerNr):
  print("sum")
  s = 0
  bits = '1'
  while bits[0] == '1':
    bits = data[index:index+5]    
    s += binToDec(data[index+1:index+5])
    index += 5
  return s, index


def run(index, part2):  
  version = binToDec(data[index:index+3])
  id = binToDec(data[index+3:index+6])        

  if part2:
    if id == 0:
      return sum(index,0)

  if id == 4:    
    return literal(index+6, version)
  else:
    if data[index+6] == '0':
      return operator15(index+6, version)      
    else:
      return operator11(index+6, version)


data = hexaToBits(data)

def part1():  
  return run(0, False)[0]
  
def part2():
  return run(0, True)
  # version = binToDec(data[index:index+3])
  # id = binToDec(data[index+3:index+6])
  # index += 6        

  # if id == 4:    
  #   return literal(index, version)
  # elif id == 0:
    
  # else:
  #   if data[index+6] == '0':
  #     return operator15(index+6, version)      
  #   else:
  #     return operator11(index+6, version)

#print(part1()) 
print(part2())