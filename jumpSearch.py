import math
def jump_search(arr, target):
    n = len(arr)
    jump = int(math.sqrt(n))
    first = 0
    while arr[min(jump, n) - 1] < target:
        first = jump
        jump += int(math.sqrt(n))
        if first >= n:
            return -1
    for i in range(first, min(jump, n)):
        if arr[i] == target:
            return i
    return -1
