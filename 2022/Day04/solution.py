from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()
    data = [i.split(",") for i in data]


def overlap(pair, fullyOverlap):
    sum = 0
    for p in pair:
        span1 = [int(section) for section in p[0].split("-")]
        span2 = [int(section) for section in p[1].split("-")]
        if (fullyOverlap and ((span1[0] <= span2[0] and span1[1] >= span2[1]) or (span2[0] <= span1[0] and span2[1] >= span1[1]))):
            sum += 1
        elif (not fullyOverlap and (span1[0] <= span2[1] and span1[1] >= span2[0])):
            sum += 1
    return sum


def part1(pair):
    return overlap(pair, True)


def part2(pair):
    return overlap(pair, False)


print(part1(data))
print(part2(data))
