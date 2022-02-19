with open('AOC_data_03.txt') as f:
    diag_report = f.read().replace('\n', ' ').split(' ')


bin_len = len(diag_report[0])


def part1():
    most_com = ''
    least_com = ''
    gamma_rate = 0
    epsilon_rate = 0

    for i in range(bin_len):
        count_0, count_1 = 0, 0
        for bin_num in diag_report:
            if bin_num[i] == '0':
                count_0 += 1 
            else:
                count_1 += 1

        most_com += '0' if count_0 > count_1 else '1'
        least_com += '1' if count_0 > count_1 else '0'

    for i in range(bin_len):
        gamma_rate += int(most_com[i]) * pow(2, bin_len - i - 1)
        epsilon_rate += int(least_com[i]) * pow(2, bin_len - i - 1)

    return gamma_rate * epsilon_rate

def part2():
    oxy_gen_rating = diag_report.copy()
    C02_scr_rating = diag_report.copy()

    while len(oxy_gen_rating) != 1:
        for i in range(bin_len):
            count_0, count_1 = 0, 0
            if (len(oxy_gen_rating) == 1):
                break

            for bin_num in oxy_gen_rating:
                if bin_num[i] == '0':
                    count_0 += 1 
                else:
                    count_1 += 1
            
            comm = '0' if count_0 > count_1 else '1'

            oxy_gen_rating = list(filter(lambda val: val[i] == comm, oxy_gen_rating))

    oxy_gen_rating = oxy_gen_rating[0]

    while len(C02_scr_rating) != 1:
        for i in range(bin_len):
            count_0, count_1 = 0, 0
            if (len(C02_scr_rating) == 1):
                break

            for bin_num in C02_scr_rating:
                if bin_num[i] == '0':
                    count_0 += 1 
                else:
                    count_1 += 1
            
            comm = '1' if count_0 > count_1 else '0'

            C02_scr_rating = list(filter(lambda val: val[i] == comm, C02_scr_rating))
        
    C02_scr_rating = C02_scr_rating[0]

    oxy, co2 = 0, 0

    for i in range(len(oxy_gen_rating)):
        oxy += int(oxy_gen_rating[i]) * pow(2, len(oxy_gen_rating) - i - 1)


    for i in range(len(C02_scr_rating)):
        co2 += int(C02_scr_rating[i]) * pow(2, len(C02_scr_rating) - i - 1)
    
    return oxy * co2


       



print(part1())
print(part2())

