from pathlib import Path
import pytest
from collections import defaultdict

def solve(input):

    ans1 = None
    ans2 = None

    file_sizes = defaultdict(int)
    current_dir = Path("/")


    for i, line in enumerate(input.split('\n')):
      
        if line != "":
            splitted = line.split(" ")
            if splitted[0] == "$":
                if splitted[1] == "cd":
                    current_dir = (current_dir / splitted[2]).resolve()

                elif splitted[1] == "ls":
                    ...

            elif splitted[0] == "dir":
                ...
            else:
                size = int(line.split(" ")[0])
                file_sizes[current_dir] += size
                for parent in current_dir.parents:
                    file_sizes[parent] += size
    
    ans1 = sum(v for v in file_sizes.values() if v <= 100000)

    unused_space = file_sizes[Path("C:/")]
    required = 30000000 - (70000000 - unused_space)

    ans2 = min(v for v in file_sizes.values() if v >= required)

    return ans1, ans2

test_input = \
"""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

# expected_output = [None, None]
expected_output = [95437, 24933642]

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
