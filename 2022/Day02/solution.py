from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()
    data = [i.split(" ") for i in data]

convert = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

points = {
    "A": 1,
    "B": 2,
    "C": 3,
}

win = {
    "A": "B",
    "B": "C",
    "C": "A"
}

loss = {
    "A": "C",
    "B": "A",
    "C": "B"
}


def get_round_score(p1, p2):
    if (p1 == p2):
        return 3 + points[p2]
    elif (win[p1] == p2):
        return 6 + points[p2]
    return points[p2]


def part1(rounds):
    return sum([get_round_score(round[0], convert[round[1]]) for round in rounds])


def part2(rounds):
    sum = 0
    for round in rounds:
        p1 = round[0]
        p2 = round[1]

        if (p2 == "X"):
            sum += get_round_score(p1, loss[p1])
        elif (p2 == "Y"):
            sum += get_round_score(p1, p1)
        else:
            sum += get_round_score(p1, win[p1])
    return sum


print(part1(data))
print(part2(data))
