from pathlib import Path
import pytest

# --- SOLUTION ------------------------------------------------------------------------------------------------- #
# Run: py -m Day_08.main
#

def solve(input):

    ans1 = None
    ans2 = None

    input = input.strip().split("\n")

    count = 0
    score_list = []

    storage = []

    for line in input:
        if line != "":
            vert = []
            for char in line:
                vert.append(int(char))
            storage.append(vert)

    for y, hor in enumerate(storage):
        for x, val in enumerate(hor):

            tree = int(val)

            topslice = [h[x] for h in storage[:y]]
            botslice = [h[x] for h in storage[y+1:]]
            leftslice = hor[:x]
            rightslice = hor[x+1:]
            # Part 1
            if all ([len(topslice)>0, len(botslice)>0, len(leftslice)>0, len(rightslice)>0]):
                if any ([tree > max(topslice), tree > max(botslice), tree > max(leftslice), tree > max(rightslice)]):
                    count += 1
            else:
                count += 1

            # Part 2
            if any ([len(topslice)==0, len(botslice)==0, len(leftslice)==0, len(rightslice)==0]):
                score_list.append(0)
            else:
                top_ = []
                for t in topslice[::-1]:
                    top_.append(t)
                    if t >= tree:
                        break

                bot_ = []
                for b in botslice:
                    bot_.append(b)
                    if b >= tree:
                        break

                left_ = []
                for l in leftslice[::-1]:
                    left_.append(l)
                    if l >= tree:
                        break

                right_ = []
                for r in rightslice:
                    right_.append(r)
                    if r >= tree:
                        break

                score_list.append(len(top_)*len(bot_)*len(left_)*len(right_))

    ans1 = count
    ans2 = max(score_list)

    return ans1, ans2


# --- TEST -------------------------------------------------------------------------------------------------- #
# Run: pytest Day_08/main.py
#

test_input = """30373
25512
65332
33549
35390
"""
expected_output = [21, 8]

@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (test_input, expected_output),
    ),
)
def test (input_s, expected) -> None:
    assert solve (input_s) == tuple(expected)



if __name__ == "__main__":
    INPUT_TEXT = Path(Path(__file__).parent / "input.txt").read_text()

    ans, ans2 = solve(INPUT_TEXT)
    print("Part 1: ", ans)
    print("Part 2: ", ans2)
