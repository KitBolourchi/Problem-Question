str = 'tactcoa'


def palindrome_permutation(str):
    new_str = str.replace(' ', '')
    my_dict = {}
    is_odd = 0
    for c in new_str:
        if c not in my_dict:
            my_dict[c] = 1
        else:
            my_dict[c] += 1

    for i in my_dict:
        if my_dict.get(i) % 2 != 0:
            is_odd +=1

    return is_odd <= 1
    


print(palindrome_permutation(str))