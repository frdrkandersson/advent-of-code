from os.path import abspath, dirname, join
import copy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open(abspath(join(dirname(__file__), 'input_sample.txt')), 'r') as f:
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

# def literal(packet):  
#   print(f"literal: {packet}")  
#   s = ""
#   pos = 0
#   while True:
#     bits = packet[pos:pos+5]    
#     s += bits[1:5]
#     pos += 5
#     if bits[0] == '0':
#       break          
#   return(binToDec(s), pos+6)

# def operator(packet):  
#   print(f"operator: {packet}")  
#   sumVerNr = 0  
#   typeId = 15 if packet[0] == '0' else 11
#   if typeId == 15:
#     totalLength = packet[1:16]    
#     subPackets = packet[16:16+binToDec(totalLength)]    
#     #print(subPackets)
#     print(f"15: {subPackets}")
#     while True:            
#       s, subPackets = runNextPacket(subPackets)
#       sumVerNr += s            
#       if len(subPackets) == 0:
#         break      
#   else:    
#     numberOfSubs = binToDec(packet[1:12])
#     subPackets = packet[12:]
#     i = 0
#     print(f"11: {numberOfSubs}")
#     while i < numberOfSubs:      
#       s, subPackets = runNextPacket(subPackets)
#       sumVerNr += s
#       i += 1    
#   return sumVerNr, subPackets

# def runNextPacket(packet):    
#   print(f"runNext {packet}")  
#   sumVerNr = binToDec(packet[:3])
#   id = binToDec(packet[3:6])    
#   start = packet[6:]

#   # if len(start) == 0:
#   #   return sumVerNr, ""      
#   if id == 4:
#     _, endPos = literal(start)
#     futurePackets = packet[endPos:] 
#   else:
#     v, futurePackets = operator(start)
#     print(v)
#     sumVerNr += v
    
#   futurePackets.lstrip("0")  
#   return sumVerNr, futurePackets

def runNextPacket(packet):  
    sumVerNr = binToDec(packet[:3])
    id = binToDec(packet[3:6])
    if id == 4:
        _, endPos = literal(start)
        futurePackets = packet[endPos:] 
        
def run(data):  
    sumVerNr = 0
    packets = hexaToBits(data)
    print(packets)
    while True:
        vernr, packets = runNextPacket(packets)

#   while True:    
#     vernr, packets = runNextPacket(packets)    
#     sumVerNr += vernr
#     # if len(packets.strip("0")) != 0 or len(packets) < 6:
#     #   break
#     if len(packets.strip("0")) == 0:
#       break
#   return sumVerNr

def part1(data):
  return run(data)
  

# def part2(data):
#   return ""

print(part1(data)) 
# print(part2(data))