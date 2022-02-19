arr = [0, 1, 0, 1, 1, 0, 1, 1]

def solution(A):
    max = 1000000000
    pairs = 0
    zero_count = 0

    for n in A:
        if n == 0:
            zero_count += 1
        else:
            pairs += zero_count
    
    if pairs > max:
        return -1
    else:
        return pairs

print(solution(arr))


        