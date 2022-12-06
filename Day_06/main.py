from pathlib import Path

sample_input = \
"""mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

def solve (input):

    ans1 = None
    ans2 = None

    instr = input

    actual_count_1 = 0

    contain = set([])
    for char in instr:

        if len(contain) == 4:
            break

        if char in contain:
            contain = set([])
        else:
            contain.add(char)

        actual_count_1 += 1

    actual_count_2 = 0

    contain = set([])
    for char in instr:

        if len(contain) == 14:
            break

        if char in contain:
            contain = set([])
        else:
            contain.add(char)

        actual_count_2 += 1


    ans1 = actual_count_1
    ans2 = actual_count_2

    return ans1, ans2

if __name__ == "__main__":
    try:
        input = Path("Day_06/input.txt").read_text()
    except:
        input = sample_input
    
    p1, p2 = solve (input)

    print("Part 1: ", p1)
    print("Part 2: ", p2)