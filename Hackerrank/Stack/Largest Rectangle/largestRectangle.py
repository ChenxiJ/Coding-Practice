def largestRectangle(h):
    s = []
    ans = len(h)
    h.append(0)

    for i in range(len(h)):
        leftIndex = i
        while len(s) > 0 and s[-1][0] >= h[i]:
            # when new building is shorter or equal to the one before, means can merge
            last = s.pop()
            leftIndex = last[1]
            # max area is either the peak one, when s[-1][0] is very high
            ans = max(ans, h[i] * (i + 1 - last[1]))
            # or max is the lower height after the peak but merged as left as possible
            ans = max(ans, last[0] * (i - last[1]))
        # put all the index and building height in a stack
        s.append((h[i], leftIndex))

    return ans