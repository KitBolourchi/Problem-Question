arr = [1, 3, 6, 4, 1, 2]

def solution(A):
    my_dict = {}

    for n in range(1, max(arr) + 1):
        my_dict[n] = n
    
    for n in my_dict:
        if n not in A:
            return n
    
    return n + 1

# print(solution(arr)),

# def solution(A):
#     sorted_num = sorted(A)
#     if sorted_num[-1] < 0 or sorted_num[0] > 1:
#         return 1

#     for i in range(1, len(sorted_num)):
#         if sorted_num[i-1] == sorted_num[i]:
#             continue
#         elif sorted_num[i-1] != sorted_num[i] - 1:
#             return sorted_num[i-1] + 1
        
#     return sorted_num[-1] + 1


# def solution(A):
#     A.sort()
#     min = 1

#     for n in A:
#         if n == min:
#             min += 1

#     return min


print(solution(arr))