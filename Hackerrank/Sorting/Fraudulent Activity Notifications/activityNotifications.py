from collections import deque

class RunningCountSortMedian():
    def __init__(self, maxValue, lookbackDays):
        self.count = [0] * (maxValue + 1)
        self.queue = deque()
        self.lookbackDays = lookbackDays

    def add(self, val):
        self.queue.append(val)
        self.count[val] += 1
        if len(self.queue) > self.lookbackDays:
            delVal = self.queue.popleft()
            self.count[delVal] -= 1

    def countSortMedian(self):
        # start from the most middle 2 (position) elements in queue
        indexA = self.lookbackDays // 2
        indexB = indexA + 1
        mid1 = None
        mid2 = None
        sum = 0
        # find the index of the most middle (value) elements
        for idx, value in enumerate(self.count):
            sum += value
            if sum >= indexA and mid1 is None:
                mid1 = idx
            if sum >= indexB:
                mid2 = idx
                break

        if self.lookbackDays % 2 == 0:
            # keep float             
            return (mid1 + mid2) / 2
        else:
            return mid2

        
def activityNotifications(expenditure, d):
    notifications = 0
    countSort = RunningCountSortMedian(200, d)
    for i in expenditure[:d]:
        countSort.add(i)
        
    for idx, value in enumerate(expenditure[d:]):
        median = countSort.countSortMedian()
        if value >= (2 * median):
            notifications += 1
        countSort.add(value)
        
    return notifications