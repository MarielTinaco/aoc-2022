from pathlib import Path

input_sample = \
"""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def solve (input):  
    
    count = 0

    lines = []
    moves = []

    for i, line in enumerate(input.split('\n')):
        if line != "":
            if i < 8:
                lines.append(line)
            if i > 9:
                moves.append(line)

    initial_state = [
        [],[],[],[],[],[],[],[],[]
    ]

    for j in lines[::-1]:
        count = 0
        for k, block in enumerate(j):
            if (k - 1) % 4 == 0:
                if block != " ":
                    initial_state[count].append(block)
                count += 1

    for move in moves:
        out = move.split(' ')
        quant, source, dest = int(out[1]), int(out[3]), int(out[5])

        norm_source = source - 1
        norm_dest = dest - 1

        for _ in range(quant):
            elem = initial_state[norm_source].pop()
            initial_state[norm_dest].append(elem)

    answer = [inv[-1] for inv in initial_state]
    return ''.join(answer)


def solve_2 (input):
    
    
    count = 0

    lines = []
    moves = []

    for i, line in enumerate(input.split('\n')):
        if line != "":
            if i < 8:
                lines.append(line)
            if i > 9:
                moves.append(line)

    initial_state = [
        [],[],[],[],[],[],[],[],[]
    ]

    for j in lines[::-1]:
        count = 0
        for k, block in enumerate(j):
            if (k - 1) % 4 == 0:
                if block != " ":
                    initial_state[count].append(block)
                count += 1

    for move in moves:
        out = move.split(' ')
        quant, source, dest = int(out[1]), int(out[3]), int(out[5])

        norm_source = source - 1
        norm_dest = dest - 1

        tomove = [initial_state[norm_source].pop() for _ in range(quant)]

        for elem in tomove[::-1]:
            initial_state[norm_dest].append(elem)

    answer = [inv[-1] for inv in initial_state]
    return ''.join(answer)

if __name__ == "__main__":
    try:
        input = Path("Day_05/input.txt").read_text()
    except:
        input = input_sample

    ans = solve(input)
    print("Part 1: ", ans)

    ans = solve_2(input)
    print("Part 2: ", ans)

