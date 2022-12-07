from pathlib import Path
import pytest

def solve (input):

    ans1 = None
    ans2 = None

    instr = input

    actual_count_1 = 0
    actual_count_2 = 0

    contain = set([])

    for i, char in enumerate(instr):

        # if len(contain) == 14:
        #     actual_count_2 = i + 1

        if char in contain:
            contain = set([])
        else:
            contain.add(char)

        if len(contain) == 4:
            actual_count_1 = i + 1

    ans1 = actual_count_1
    ans2 = actual_count_2

    return ans1, ans2

test_input = \
"""mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
expected_output = 7

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (test_input, expected_output),
    ),
)
def test (input_s, expected) -> None:
    ans1, ans2 = solve (input_s)
    assert ans1 == expected


if __name__ == "__main__":

    input = Path("Day_06/input.txt").read_text()
    
    p1, p2 = solve (input)

    print("Part 1: ", p1)
    print("Part 2: ", p2)