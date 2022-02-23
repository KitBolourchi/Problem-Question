# # Write a function:

# class Solution { public int solution(int N); }
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001

n = 1041

def solution(N):
    bina = bin(N)
    current = 0
    longest = 0
    for b in bina[2:]:
        if int(b) == 0:
            current += 1
        elif int(b) == 1:
            longest = max(current, longest)
            current = 0

    return longest


print(solution(n))