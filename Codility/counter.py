arr = [3, 4, 4, 6, 1, 4, 4]

# def solution(N, A):
#     max = 0
#     my_counters = {}
#     for c in range(1, N+1):
#         my_counters[c] = 0
#     for num in arr:
#         if num > N:
#             for item in my_counters:
#                 my_counters[item] = max
#         else:
#             my_counters[num] += 1
#             if my_counters[num] > max:
#                 max = my_counters[num]
    
#     final = []
#     for key, value in my_counters.items():
#         final.append(value)
#     return final

def solution(N, A):
    max = 0
    my_counters = N * [0]
    last_update = 0
    
    for num in A:
        if num > N:
            last_update = max
        else:
            if my_counters[num-1] < last_update:
                my_counters[num-1] = last_update
                
            my_counters[num-1] += 1
            if my_counters[num-1] > max:
                max += 1
    
    for i in range(len(my_counters)):
        if my_counters[i] < last_update:
            my_counters[i] = last_update

    return my_counters
    
    

print(solution(5, arr))
