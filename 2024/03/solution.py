import re
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read()

def part1(input):
    result = 0
    operations = re.findall(r"mul\(\d+,\d+\)", input)

    for mul in operations:
        operands = mul[4:-1].split(",")
        result += int(operands[0]) * int(operands[1])

    return result

def part2(input):
    result = 0
    conditional = re.split(r"do", input)

    for c in conditional:
        result += 0 if c.startswith("n't") else part1(c)

    return result

print(part1(data))
print(part2(data))