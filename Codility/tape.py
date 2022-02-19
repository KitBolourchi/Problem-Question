from itertools import accumulate


arr = [3, 1, 2, 4, 3]

# def solution(A):
#     forward_list = []
#     backward_list = []
#     count = 0
#     for n in range(len(A) - 1):
#         count += A[n]
#         forward_list.append(count)
    
#     count = 0
#     for p in A[:0:-1]:
#         count += p
#         backward_list.append(count)
    
#     len_b = len(backward_list) - 1
#     current_diff = abs(forward_list[0] - backward_list[-1])
#     for i in range(len(forward_list)):
#         if abs(forward_list[i]-backward_list[len_b]) < current_diff:
#             current_diff = abs(forward_list[i]-backward_list[len_b])
#         len_b -= 1
#     return current_diff


def solution(A):
    s = sum(A)
    l = list(accumulate(A[:-1]))
    minimum = abs(2*l[0] - s)
    for x in l:
        current = abs(2*x - s)
        if current < minimum:
            minimum = current
    return minimum
        


print(solution(arr))
        