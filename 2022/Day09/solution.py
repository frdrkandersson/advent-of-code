from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input2.txt')), 'r') as f:
    data = f.read().splitlines()
    data = [row.split() for row in data]


def createRope(len):
    return [[0, 0] for _ in range(0, len)]


def move_tail(rope, direction):
    for i in range(0, len(rope)-1):
        head = rope[i]
        tail = rope[i+1]
        distance = abs(head[0]-tail[0]) + abs(head[1]-tail[1])

        if distance < 2:
            continue

        if direction == "R":
            if head[1] == tail[1]:
                tail[0] = head[0]-1
            elif distance > 2:
                tail[0] = head[0]-1
                tail[1] = head[1]
        elif direction == "L":
            if head[1] == tail[1]:
                tail[0] = head[0]+1
            elif distance > 2:
                tail[0] = head[0]+1
                tail[1] = head[1]
        elif direction == "U":
            if head[0] == tail[0]:
                tail[1] = head[1]-1
            elif distance > 2:
                tail[1] = head[1]-1
                tail[0] = head[0]
        elif direction == "D":
            if head[0] == tail[0]:
                tail[1] = head[1]+1
            elif distance > 2:
                tail[1] = head[1]+1
                tail[0] = head[0]
    return rope


def move(rope, visited, direction, distance):
    for _ in range(distance):
        head = rope[0]
        if direction == "R":
            head[0] += 1
        elif direction == "L":
            head[0] -= 1
        elif direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1

        rope = move_tail(rope, direction)
        #print((rope[-1][0], rope[-1][1]))
        visited.add((rope[-1][0], rope[-1][1]))
    return rope, visited


def part1(data):
    visited = set()
    rope = createRope(2)
    for step in data:
        rope, visited = move(rope, visited, step[0], int(step[1]))
    return len(visited)


def part2(data):
    visited = set()
    rope = createRope(10)
    for step in data:
        rope, visited = move(rope, visited, step[0], int(step[1]))
    print(visited)
    return len(visited)


print(part1(data))
print(part2(data))
