with open('AOC_data_03.txt') as f:
    binary = f.readlines()


def part1(input):
    count = 0
    gamma = []
    epsilon = []
    count_0 = 0
    count_1 = 0
    while count < len(input[1])- 1:
        for b in input:
            for d in b[count:count+1]:
                if d == '1':
                    count_1 += 1
                elif d == '0':
                    count_0 += 1
        count += 1
        if count_1 > count_0:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
        count_0, count_1 = 0, 0
    print(gamma)
    print(epsilon)
    
    g_value = 0
    e_value = 0
    for i in range(len(gamma)):
        digit = gamma.pop()
        if digit == 1:
            g_value = g_value + pow(2, i)

    for i in range(len(epsilon)):
        digit = epsilon.pop()
        if digit == 1:
            e_value = e_value + pow(2, i)
    return g_value * e_value


        
print(part1(binary))

