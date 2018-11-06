def pylons(k, arr):
    count = 0
    exploreFrom = 0
    lastPut = [-1]

    while exploreFrom < len(arr):
        # pay attention to the intro that range k means less than k, so the -1 
        # is important as the range also include the city itself, so right range has to -1
        right = min(exploreFrom + k - 1, len(arr) - 1)
        for put in range(right, lastPut[-1], -1):
            if arr[put] == 1:
                count += 1
                exploreFrom = put + k
                lastPut.append(put)
                break
        if exploreFrom != put + k:
            return -1
    return count