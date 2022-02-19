arr = []

def solution(A):
    sorted_list = sorted(A)
    if len(arr) == 0 or sorted_list[0] != 1:
        return 1
    for i in range(len(sorted_list) - 1):
        if sorted_list[i+1] != sorted_list[i] + 1:
            return sorted_list[i] + 1
    return len(A) + 1



print(solution(arr))