# Given two strings, write a method to decide if one is a permutation of the other.
string_1 = 'abcd'
string_2 = 'dcbw'


# def isPermutation(str_1, str_2):
#     counter = 0
#     if len(str_1) != len(str_2):
#         return False
#     for i in str_1:
#         for j in str_2:
#             if i == j:
#                 count += 1
#     if count == len(str_1):
#         return True
#     else:
#         return False

def isPermutation(str_1, str_2):
    count = {}
    if len(str_1) != len(str_2):
        return False
    for char in str_1:
        count[char] = 1
    for char in str_2:
        if char not in count:
            return False
    return True


# def isPermutation(str_1, str_2):
#     sorted_str_1, sorted_str_2 = sorted(str_1), sorted(str_2)
#     return sorted_str_1 == sorted_str_2


print(isPermutation(string_1, string_2))
