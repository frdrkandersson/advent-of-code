from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()
    data = [list(row) for row in data]
    for y in range(len(data)):
        for x in range(len(data[0])):
            data[x][y] = int(data[x][y])


def left(x, y):
    distance = 0
    for x_local in range(x-1, -1, -1):
        distance += 1
        if data[y][x_local] >= data[y][x]:
            return (False, distance)
    return (True, distance)


def right(x, y):
    distance = 0
    for x_local in range(x+1, len(data[0])):
        distance += 1
        if data[y][x_local] >= data[y][x]:
            return (False, distance)
    return (True, distance)


def up(x, y):
    distance = 0
    for y_local in range(y-1, -1, -1):
        distance += 1
        if data[y_local][x] >= data[y][x]:
            return (False, distance)
    return (True, distance)


def down(x, y):
    distance = 0
    for y_local in range(y+1, len(data)):
        distance += 1
        if data[y_local][x] >= data[y][x]:
            return (False, distance)
    return (True, distance)


def getCount():
    count = 0
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            if left(x, y)[0] or right(x, y)[0] or up(x, y)[0] or down(x, y)[0]:
                count += 1
    return count


def getDistance():
    distances = []
    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            distances.append(left(x, y)[1] * right(x, y)
                             [1] * up(x, y)[1] * down(x, y)[1])
    return max(distances)


def part1():
    return getCount()


def part2():
    return getDistance()


print(part1())
print(part2())
