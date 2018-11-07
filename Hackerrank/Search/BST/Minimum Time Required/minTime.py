# given a number of days, see how many products can be made in these days
def findItems(arr, temp):
    ans = 0
    for i in range(len(arr)):
        ans += temp // arr[i]
    return ans

def binarySearch(arr, m, high):
    low = 1
    while low < high:

        mid = low + ((high - low) // 2)
        itm = findItems(arr, mid)
        if itm < m:
            low = mid + 1
        else:
            high = mid
    return high


def minTime(machines, goal):
    maxVal = 0
    for i in machines:
        maxVal = max(maxVal, i)
    # find the high of the BST range, maxVal * goal guaranteed highest days possibly needed
    return binarySearch(machines, goal, maxVal * goal)