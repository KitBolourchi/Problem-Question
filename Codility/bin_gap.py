num = '10001001001011100100'

def solution(N):
    current = 0
    longest = 0
    for n in N:
        if int(n) == 0:
            current += 1
        elif current >= longest:
            longest = current
            current = 0
        else:
            current = 0
    return longest

print(solution(num))