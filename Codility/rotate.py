my_list = [1, 2, 3 ,4]

def solution(A ,K):
    while K != 0:
        for i in range(len(A)):
            A[i], A[-1] = A[-1], A[i]
        K -= 1
    return A

print(solution(my_list, 6))