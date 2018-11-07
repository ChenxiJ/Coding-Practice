def merge(arr, low, middle, high):
    # first half arr[low:middle + 1], second half arr[middle + 1: high + 1]
    lenFirst = middle - low + 1
    lenSecond = high - middle

    # create temp arrays
    firstHalf = arr[low:middle + 1]
    secondHalf = arr[middle + 1: high + 1]

    # merge the temp arrays back to arr[low: high + 1]
    firstIndex = 0
    secondIndex = 0
    mergeIndex = low

    while firstIndex < lenFirst and secondIndex < lenSecond:
        if firstHalf[firstIndex] <= secondHalf[secondIndex]:
            arr[mergeIndex] = firstHalf[firstIndex]
            firstIndex += 1
        else:
            arr[mergeIndex] = secondHalf[secondIndex]
            secondIndex += 1
        mergeIndex += 1
    # copy the rest elements in firstHalf and secondHalf back to arr
    while firstIndex < lenFirst:
        arr[mergeIndex] = firstHalf[firstIndex]
        firstIndex += 1
        mergeIndex += 1
    while secondIndex < lenSecond:
        arr[mergeIndex] = secondHalf[secondIndex]
        secondIndex += 1
        mergeIndex += 1


def mergeSort(arr, low, high):
    if low < high:
        # same as (low + high) // 2, but avoid overflow for large low and high
        middle = low + (high - low) // 2
        mergeSort(arr, low, middle)
        mergeSort(arr, middle + 1, high)
        merge(arr, low, middle, high)
    return arr