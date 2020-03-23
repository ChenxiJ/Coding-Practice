import sys

# important message here is that the elements can be negative!! often will ignore cases like this


def max_subarray_subsequence(arr):
    all_negative = True
    sum_subsequence = 0
    sum_subarray = arr[0]
    max_subarray = arr[0]
    max_subsequence = -sys.maxsize
    for i in range(len(arr)):
        if arr[i] >= 0:
            sum_subsequence += arr[i]
            all_negative = False
        else:
            if all_negative:
                max_subsequence = max(arr[i], max_subsequence)
        if i > 0:
            sum_subarray = max(arr[i], sum_subarray + arr[i])
            max_subarray = max(sum_subarray, max_subarray)
    ans1 = max_subsequence if all_negative else sum_subsequence

    return [max_subarray, ans1]
