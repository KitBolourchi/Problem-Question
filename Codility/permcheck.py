arr = [1, 2, 4]

# def solution(A):
#     my_dict = {}
#     count = max(A)
#     for n in A:
#         if n not in my_dict:
#             my_dict[n] = n
#             count -= 1
#         else:
#             return 0
#     if count == 0:
#         return 1
#     else:
#         return 0

def solution(A):
    A.sort()
    if A[0] != 1:
        return 0
    
    for num in range(1, len(A)):
        if A[num] != A[num-1] + 1:
            return 0
    return 1


print(solution(arr))


