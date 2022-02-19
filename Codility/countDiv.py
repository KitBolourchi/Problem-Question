min_n = 5
max_n = 11
divis = 2

# def solution(A, B, K):
#     count = 0 
#     for n in range(A, B):
#         if n % K == 0:
#             count += 1
#     return count


def solution(A, B, K):
    if A % K == 0:
        return (B - A) // K + 1
    else:
        return (B - (A - A % K)) // K

print(solution(min_n, max_n, divis))

