# quick sort, here last element as pivot
# worst case: O(n^2), when always pick the greatest or the smallest element as pivot
# best case: O(n log n), pivot always the middle one
# prefer over merge sort for arrays for it doesn't require extra O(N) storage
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # i+1 is the pivot for the next recursion, it is at the right position in the sorted array
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)
    return arr