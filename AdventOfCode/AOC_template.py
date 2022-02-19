import pathlib
import sys


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]

def part1(data):
    pass

def part2(data):
    pass

def solve(puzzle_input):
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

if __name__ == '__main__':
    for path in sys.argv[1:]:
        print(f'\n{path}:')
        puzzle_input = pathlib.Path(path).read_text().strip()

        numbers = parse(puzzle_input)
        print(part1(numbers))
        print(part2(numbers))