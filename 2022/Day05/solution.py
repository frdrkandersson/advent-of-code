from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

data_split = data.index("")


def map_stacks(stack_data):
    num_stacks = int(stack_data[-1][-1])
    result = [[] for i in range(num_stacks)]

    # loop reversed order to get from bottom to top
    for row in reversed(stack_data[:len(stack_data)-1]):
        for i in range(num_stacks):
            if i * 4 + 1 < len(row):
                crate = row[i*4+1]
                if crate != " ":
                    result[i].append(crate)
    return result


def make_move(stacks, count, move_from, move_to, crane_type):
    try:
        if crane_type == "CrateMover 9000":
            for _ in range(count):
                stacks[move_to].append(stacks[move_from][-1])
                stacks[move_from].pop()
        elif crane_type == "CrateMover 9001":
            stacks[move_to].extend(stacks[move_from][-count:])
            for _ in range(count):
                stacks[move_from].pop()
    except:
        pass
    return stacks


def apply_instructions(instructions, stacks, crane_type):
    for move in instructions:
        x = move.split(" ")
        count = int(x[1])
        move_from = int(x[3]) - 1  # 0 indexing
        move_to = int(x[5]) - 1
        stacks = make_move(stacks, count, move_from, move_to, crane_type)
    return "".join([(stack[-1]) for stack in stacks])


def part1(instructions, stacks):
    return apply_instructions(instructions, stacks, "CrateMover 9000")


def part2(instructions, stacks):
    return apply_instructions(instructions, stacks, "CrateMover 9001")


print(part1(data[data_split+1:], map_stacks(data[:data_split])))
print(part2(data[data_split+1:], map_stacks(data[:data_split])))
