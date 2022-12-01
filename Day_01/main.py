input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

if __name__ == "__main__":  


    with open ('Day_01/input.txt', 'r') as infile:
        data = [elem.split("\n")[0] for elem in infile.readlines()]

    l = []
    segment = []
    for num in data:
        if num:
            segment.append(int(num))
        else:
            l.append(segment)
            segment = []

    # Part 1

    maximum = 0
    for group in l:
        total = sum(group)
        if total > maximum:
            maximum = total

    print("Part 1 answer: ", maximum)

    # Part 2

    listed = []
    for group in l:
        total = sum(group)
        listed.append(total)

    sort = sorted(listed)
    sum_last_three = sum(sort[-3:])
    print("Part 2 answer: ", sum_last_three)
