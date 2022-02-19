#  Implement an algorithm to determine if a string has all unique characters. What if you cannot
#  use aditional data structuse?

myString = 'hello'

def checkUnique(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True



print(checkUnique(myString))

# def checkUnique(s):
#     myDict = {}
#     for c in s:
#         if c in myDict:
#             return False
#         else:
#             myDict[c] = 1
#     return True

# print(checkUnique(myString))

# def checkUnique(s):
#     sorted_str = sorted(s)
#     last_char = None
#     for c in sorted_str:
#         if c == last_char:
#             return False
#         else:
#             last_char = c
#     return True


# print(checkUnique(myString))

