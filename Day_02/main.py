from pathlib import Path

sample_input = '''A Y
B X
C Z
'''

rps_mapping = {
    'Y' : 2,    # Paper
    'X' : 1,    # Rock
    'Z' : 3     # Scissor
}

# A - ROCK
# B - Paper
# C - SCISSOR

win_condition = {
    'AY' :  6,
    'AX' :  3,
    'AZ' :  0,
    'BY' :  3,
    'BX' :  0,
    'BZ' :  6,
    'CY' :  0,
    'CX' :  6,
    'CZ' :  3
}

win_condition_2 = {
    'X' : {'A' : 'Z', 'B' : 'X', 'C' : 'Y'},
    'Y' : {'A' : 'X', 'B' : 'Y', 'C' : 'Z'},
    'Z' : {'A' : 'Y', 'B': 'Z', 'C' : 'X'}

}

def solve (input):
    
    count = 0
    for line in input.split('\n'):
        if line != "":
            cond = line.split(' ')
            joined = cond[0] + cond[1]
            score = win_condition[joined] + rps_mapping[cond[1]]
            count += score
    
    return count

def solve_2 (input):
    
    count = 0
    for line in input.split('\n'):
        if line != "":
            cond = line.split(' ')
            opponent = cond[0]
            win_con = cond[1]
            joined = cond[0] + win_condition_2[cond[1]][cond[0]]
            score = rps_mapping[win_condition_2[cond[1]][cond[0]]] + win_condition[joined]
            count += score

    
    return count
if __name__ == "__main__":
    input = Path("Day_02/input.txt").read_text()
    ans = solve(input)
    print("Part 1: ", ans)

    ans = solve_2(input)
    print("Part 2: ", ans)

