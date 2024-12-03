from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()


def get_prio(item):
    return ord(item)-38 if item.isupper() else ord(item)-96


def part1(sacks):
    result = 0
    for sack in sacks:
        c1 = set(sack[:round(len(sack)/2)])
        c2 = set(sack[round(len(sack)/2):])
        result += sum([get_prio(item) for item in c1 & c2])
    return result


def part2(sacks):
    result = 0
    for group in range(0, len(sacks), 3):
        sets = [set(g) for g in sacks[group:group+3]]
        result += sum(get_prio(item) for item in set.intersection(*sets))
    return result


print(part1(data))
print(part2(data))
