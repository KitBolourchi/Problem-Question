with open('AOC_data_02.txt') as f:
    commands = f.readlines()

def part1(commands):
    horizontal, depth = 0, 0
    for command in commands:
        dir, val = command.split(' ')[0], int(command.split(' ')[1])
        if dir == 'up':
            depth -= val
        elif dir == 'down':
            depth += val
        elif dir == 'forward':
            horizontal += val
    return horizontal * depth

def part2(commands):
    horizontal, depth, aim = 0, 0, 0
    for command in commands:
        dir, val = command.split(' ')[0], int(command.split(' ')[1])
        if  dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val
        elif dir == 'forward':
            horizontal += val
            depth += val * aim
    return horizontal * depth



print(part1(commands))
print(part2(commands))