import pathlib
import sys


def parse(puzzle_input):
    return [int(line) for line in puzzle_input.split()]

def part1(data):
    counter = 0
    previous = data[0]
    for d in data:
        if d > previous:
            counter += 1
        previous = d
    return counter

def part2(data):
    count = 0
    for i in range(len(data)-3):
        sum1 = data[i] + data[i+1] + data[i+2]
        sum2 = data[i+1] + data[i+2] + data[i+3]
        if sum2 > sum1:
            count += 1
    return count

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