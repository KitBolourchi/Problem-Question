# def one_away(str1, str2):
#     if str1 == str2:
#         return True
#     my_list = []
#     count = 0
#     for char in str1:
#         my_list.append(char)
#     for char in str2:
#         if char in my_list:
#             count += 1
#     if len(str2) > len(str1) + 1:
#         return False
#     elif count >= len(my_list )-1:
#         return True
#     else: 
#         return False

# string1 = 'pkle'
# string2 = 'ple'

# print(one_away(string1, string2))

def one_away(str_1, str_2):
    if len(str_1) == len(str_2):
        return one_edit_replace(str_1, str_2)
    if len(str_1) + 1 == len(str_2):
        return one_edit_insert(str_1, str_2)
    if len(str_1) - 1 == len(str_2):
        return one_edit_insert(str_2, str_1)

    return False

def one_edit_replace(str_1, str_2):
    edited = False
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            if edited:
                return False
            edited = True
    return True

def one_edit_insert(str_1, str_2):
    edited = False
    i, j = 0, 0
    while i < len(str_1) and j < len(str_2):
        if str_1[i] != str_2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

string1 = 'pale'
string2 = 'ple'

print(one_away(string1, string2))
