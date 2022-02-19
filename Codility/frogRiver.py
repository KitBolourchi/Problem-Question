arr = [1, 3, 1, 4, 2, 3, 5, 4, 7, 9, 6, 8]

# def solution(A , X):
#     check = []
#     store = []
#     count = 0
#     for n in range(1, X+1):
#         check.append(n)
#     for i in range(len(A)):
#         if A[i] in check and A[i] not in store:
#             store.append(A[i])
#             count += 1
#             if count == X:
#                 return i



def solution(A, X):
    leaves = {}
    count = 0
    for i in range(len(A)):
        if A[i] not in leaves and A[i] <= X:
            leaves[A[i]] = 1
            count += 1
            if count == X:
                return i
    return -1





print(solution(arr, 7))