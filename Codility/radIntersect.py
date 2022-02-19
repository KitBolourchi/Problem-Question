arr = [1, 5, 2, 1, 4, 0]

def solution(A):
    discStart = []
    discEnd = []

    for i, n in enumerate(A):
        discStart.append(i-n)
        discEnd.append(i+n)
    
    discStart.sort()
    discEnd.sort()

    openDiscs = 0
    intersections = 0
    k = 0
    listLen = len(A)

    for i in range(listLen):
        for j in range(k, listLen):
            if discStart[i] <= discEnd[j]:
                intersections += openDiscs
                if intersections > 10000000:
                    return -1
                openDiscs += 1
                break

            openDiscs -= min(1, openDiscs)
            k += 1
    
    return intersections


print(solution(arr))