from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read()


def detect(distinct_chars):
    for i in range(0, len(data)):
        s = data[i:i+distinct_chars]
        if (len(s) == len(set(s))):
            return i+distinct_chars


print(detect(4))
print(detect(14))
