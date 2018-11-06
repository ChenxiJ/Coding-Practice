# Two passes, important algorithm for finding local minimum or maximum

def candies(arr):
    # everyone gets at least one candy
    n = len(arr)
    result = [1] * n

    # first pass, from left to right
    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            result[i + 1] = result[i] + 1

    # second pass,from right to left
    for i in range(n-2, -1, -1):
        # from the back, if the child's rate is higher than the one behind, this child at least needs to be
        # given 1 more candy than the child behind. keep maximum number of 1 possible at all times
        if arr[i] > arr[i + 1] and result[i] < result[i + 1] + 1:
            result[i] = result[i + 1] + 1
    return sum(result)