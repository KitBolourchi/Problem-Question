arr = [10, 2, 5, 1, 8, 20]

def solution(A):
    A.sort()
    for i in range(2, len(A)):
        if A[i-2] + A[i-1] > A[i]:
            return 1
    return 0

print(solution(arr))