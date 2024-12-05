from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().split('\n\n')

rules = data[0].split('\n')
updates = [update.split(',') for update in data[1].split('\n')]

def get_index(list, item):
    try:
        return list.index(item)
    except:
        return -1

def is_valid_update(update, rules):
    for rule in rules:
        left, right = rule.split('|')

        left_index = get_index(update, left)
        right_index = get_index(update, right)

        if left_index < 0 or right_index < 0:
            continue

        if left_index > right_index:
            return False
    return True

def find_correct_middle(update, rules):
    while True:
        middle_index = len(update) // 2
        swappedMiddle = False
        for rule in rules:
            left, right = rule.split('|')

            left_index = get_index(update, left)
            right_index = get_index(update, right)

            if left_index != middle_index and right_index != middle_index:
                continue
            if left_index < 0 or right_index < 0:
                continue

            if left_index > right_index:
                update[left_index], update[right_index] = update[right_index], update[left_index]
                swappedMiddle = True
                continue

        if not swappedMiddle:
           break

    return update[middle_index]

valid_updates = []
invalid_updates = []
[(valid_updates if is_valid_update(update, rules) else invalid_updates).append(update) for update in updates]

part1 = lambda: sum([int(update[len(update) // 2]) for update in valid_updates])
part2 = lambda: sum([int(find_correct_middle(update, rules)) for update in invalid_updates])

print(part1())
print(part2())