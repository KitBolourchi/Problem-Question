string = "aabcccccaaa"

# def str_compression(str1):
#     my_dict = {}
#     for c in str1:
#         if c in my_dict:
#             my_dict[c] += 1
#         else:
#             my_dict[c] = 1
#     list = []
#     for char, count in my_dict.items():
#         list.append(char)
#         list.append(count)
#     new_string = ''.join(str(e) for e in list)
#     return new_string
    
# def str_compression(str1):
#     my_list = []
#     comp_str = ""
#     for i in range(len(str1)):
#         if str1[i] == str1[i - 1]:
#             my_list.append(str1[i])
#         else:
#             comp_str += my_list[0]
#             comp_str += str(len(my_list))
#             my_list = []
#             my_list.append(str1[i])
#     comp_str += my_list[0]
#     comp_str += str(len(my_list))
    
#     if len(comp_str) > len(str1):
#         return str1
#     else:
#         return comp_str

def str_compression(string):
    compressed = []
    count = 0
    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(count))
            count = 0
        count += 1
    
    if count:
        compressed.append(string[-1] + str(count))
    
    return min(string, "".join(compressed))





print(str_compression(string))

