arr = [-3, -2, 1, 2, 5, 6]

def solution(A):
    A.sort()
    p1 = A[0] * A[1] * A[-1]
    p2 = A[-1] * A[-2] * A[-3]

    return max(p1, p2)



print(solution(arr))