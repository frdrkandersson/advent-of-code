from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
  data = f.read().split(",")

data_ints = [int(i) for i in data]

def part1(data):
  data = sorted(data)
  median = data[len(data) // 2]    
  return sum([abs(i - median) for i in data])  
  
def part2(data):  
  avg = round(sum(data) // len(data))  
  return sum([sum(range(1, abs(i - avg) + 1)) for i in data])  

print(part1(data_ints))  
print(part2(data_ints))