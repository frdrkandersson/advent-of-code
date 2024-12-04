from collections import defaultdict
from os.path import abspath, dirname, join

with open(abspath(join(dirname(__file__), 'input.txt')), 'r') as f:
    data = f.read().splitlines()

sign = lambda x: bool(x > 0) - bool(x < 0)

def analyze_report(levels):
    for i, _ in enumerate(levels):
        if i >= 1 and abs(levels[i] - levels[i-1]) > 3 or abs(levels[i] - levels[i-1]) < 1:                        
            return False                        
        if i >= 2 and sign(levels[i]-levels[i-1]) != sign(levels[i-1]-levels[i-2]):            
            return False

    return True

def analyze(input, tolerate):
    sum = 0

    for report in input:
        levels = [int(x) for x in report.split()]
        safe = analyze_report(levels)
        if not safe and tolerate:
             for i, _ in enumerate(levels):
                newList = list(levels)
                del newList[i]      
                safe = analyze_report(newList)
                if safe:
                     break                                                          
                
        sum += 1 if safe else 0

    return sum

print(analyze(data, False))
print(analyze(data, True))