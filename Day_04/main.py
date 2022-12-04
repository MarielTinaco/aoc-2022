from pathlib import Path

input_sample = \
"""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def solve (input):  
    
    count = 0
    for line in input.split('\n'):
        if line != "":
            pair = line.split(',')
            set_from_range = lambda x : set([int(i) for i in range(int(x[0]), int(x[1])+1)])
            set1 = set_from_range(pair[0].split('-'))
            set2 = set_from_range(pair[1].split('-'))

            if set1.issubset(set2) or set2.issubset(set1):
                count += 1

    return count

def solve_2 (input):
    
    count = 0
    for line in input.split('\n'):
        if line != "":
            pair = line.split(',')
            set_from_range = lambda x : set([int(i) for i in range(int(x[0]), int(x[1])+1)])
            set1 = set_from_range(pair[0].split('-'))
            set2 = set_from_range(pair[1].split('-'))

            if set1.intersection(set2):
                count += 1

    return count

if __name__ == "__main__":
    input = Path("Day_04/input.txt").read_text()

    ans = solve(input)
    print("Part 1: ", ans)

    ans = solve_2(input)
    print("Part 2: ", ans)

