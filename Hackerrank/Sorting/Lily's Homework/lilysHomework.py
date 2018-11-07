def swap(arr):
    count = 0
    mapp = {}
    # first save the index of the elements to a dict, then sort the array
    for i in range(len(arr)):
        mapp[arr[i]] = i
    sortedArr = sorted(arr)
    for i in range(len(arr)):
        if arr[i] != sortedArr[i]:
            count += 1
            mapp[arr[i]] = mapp[sortedArr[i]]
            arr[i], arr[mapp[sortedArr[i]]] = arr[mapp[sortedArr[i]]], arr[i]
    return count


def lilysHomework(arr):
    return min(swap(arr), swap(list(reversed(arr))))