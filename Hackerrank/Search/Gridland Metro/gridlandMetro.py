def mergeRow(arr):
    if len(arr) == 1:
        return [[arr[0][0], arr[0][1]]]
    else:
        arr.sort(key=lambda x: x[0])
        newArr = []
        left = arr[0][0]
        right = arr[0][1]

        for i in range(len(arr) - 1):
            a = arr[i + 1][0]
            if arr[i + 1][0] - right <= 1:
                right = max(arr[i + 1][1], right)
            else:
                newArr.append([left, right])
                left = arr[i + 1][0]
                right = arr[i + 1][1]
        newArr.append([left, right])
        return newArr


def gridlandMetro(n, m, k, track):
    trackCell = 0
    mapp = {}
    for i in range(k):
        currentTrack = track[i]
        if currentTrack[0] in mapp:
            mapp[currentTrack[0]].append([currentTrack[1], currentTrack[2]])
        else:
            # pay attention when value is a list, don't forget to put []
            mapp[currentTrack[0]] = [[currentTrack[1], currentTrack[2]]]
    for i in mapp:
        # tracks can overlap, so need to merge to non-overlapping tracks for each row for the right count
        newRow = mergeRow(mapp[i])
        for j in range(len(newRow)):
            trackCell += newRow[j][1] - newRow[j][0] + 1
    return n * m - trackCell