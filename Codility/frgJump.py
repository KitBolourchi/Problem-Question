X = 10
Y = 80
D = 30

# def solution(X, Y, D):
#     jumps = 0
#     while X < Y:
#         X += D
#         jumps += 1
#     return jumps

# print(solution(X, Y, D))


def solution(X, Y, D):
    result = (Y - X) // D
    if (Y - X) % D == 0:
        return result
    else:
        return result + 1

print(solution(X, Y, D))