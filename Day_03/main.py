from pathlib import Path

input_sample = \
"""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve (input):  
    
    count = 0
    for line in input.split('\n'):
        if line != "":
            halflength = int(len(line)/2)
            firsthalf = line[:halflength]
            secondhalf = line[halflength:]

            assert (len(firsthalf) == len(secondhalf))

            common = list(set(firsthalf)&set(secondhalf))
            val = alpha.index(common[0]) + 1
            count += val
    
    return count

def solve_2 (input):
    
    list_all = []
    cluster = []

    count = 0

    for i, line in enumerate(input.split('\n')):
        if line != "":
            cluster.append(line)
            if (i + 1) % 3 == 0:
                list_all.append(cluster)
                common = list(set(cluster[0])&set(cluster[1])&set(cluster[2]))
                val = alpha.index(common[0]) + 1
                count += val
                cluster = []

    return count

if __name__ == "__main__":
    input = Path("Day_03/input.txt").read_text()

    ans = solve(input)
    print("Part 1: ", ans)

    ans = solve_2(input)
    print("Part 2: ", ans)

