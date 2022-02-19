arr = [9, 3, 9, 3, 9, 7, 9, 7, 7]

def solution(A):
    dict = {}
    for n in A:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    
    for key, value in dict.items():
        if value % 2 != 0:
            return key

print(solution(arr))