from collections import defaultdict
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()    

left, right = zip(*[x.split("   ") for x in data])

left = list(left)
left.sort()

right = list(right)
right.sort()

def part1():
    sum = 0

    for i, _ in enumerate(left):
        sum += abs(int(left[i]) - int(right[i]))        

    return sum

def part2():    
    numbers = defaultdict(int)
    result = 0

    for num in right:      
      numbers[num] += 1
    
    for _, num in enumerate(left):                
        result += int(num) * numbers[num]

    return result

print(part1())
print(part2())