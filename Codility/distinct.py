arr = [2, 1, 1, 2, 3, 1]

# def solution(A):
#     my_dict = {}
#     count = 0
#     for n in A:
#         if n not in my_dict:
#             my_dict[n] = n
#             count += 1
#     return count

def solution(A):
    return len(set(A))

print(solution(arr))                                                                                   


