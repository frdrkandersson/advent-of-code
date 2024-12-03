from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split("\n\n")
    data = [i.split("\n") for i in data]


def part1(inputs):
    sums = [sum((int(food) for food in elf)) for elf in inputs]
    return sums


def part2(inputs):
    sums = sorted(part1(inputs), reverse=True)
    return sum(sums[:3])


print(max(part1(data)))
print(part2(data))
