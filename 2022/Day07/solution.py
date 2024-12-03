from os.path import abspath, dirname, join
from collections import defaultdict

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

current_path = "/"
dir_tree = defaultdict(list)
seen_file = set()
dir_sizes = defaultdict(int)


def get_dir():
    global current_path
    index = current_path.rfind("/")
    x = current_path[index + 1:]
    x = x if x != "" else "/"
    return x


def cd(folder):
    global current_path
    if folder == "/":
        current_path = "/"
    elif folder == "..":
        parent = current_path.rfind("/")
        current_path = current_path[:parent]
        current_path = current_path if current_path != "" else "/"
    else:
        if current_path != "/":
            current_path += "/"
        current_path += folder


def execute_command(cmd):
    if cmd.startswith("cd "):
        cd(cmd[3:])


def apply_size_to_parents(size):
    global current_path
    saved_current_path = current_path
    while True:
        cd("..")
        dir_sizes[current_path] += int(size)
        if current_path == "/":
            current_path = saved_current_path
            break


def parse_row(row):
    curr_dir = get_dir()
    if row.startswith("$ "):
        execute_command(row[2:])
    elif row.startswith("dir "):
        dir_name = row[4:]
        if dir_name not in dir_tree[curr_dir]:
            dir_tree[curr_dir].append(dir_name)
    else:
        size, name = row.split()
        file_path = current_path + "/" + name
        if file_path not in seen_file:
            seen_file.add(file_path)
            dir_sizes[current_path] += int(size)
            if curr_dir != "/":
                apply_size_to_parents(size)


def part1():
    return sum([v if v <= 100000 else 0 for v in dir_sizes.values()])


def part2():
    size_to_free_up = 30000000 - (70000000 - dir_sizes["/"])
    smallest_dir = ("", 9999999999999999)
    for k, v in dir_sizes.items():
        if v >= size_to_free_up and v < smallest_dir[1]:
            smallest_dir = (k, v)
    return smallest_dir[1]


[parse_row(row) for row in data]
print(part1())
print(part2())
