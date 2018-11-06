def hackerlandRadioTransmitters(x, k):
    x.sort()
    count = 0
    i = 0
    while i < len(x):
        location = x[i] + k
        while i < len(x) and x[i] <= location:
            i += 1
        i -= 1
        # place transmitter here at x[i]
        count += 1
        # here is important, after putting the transmitter, the range on the
        # right side we don't need to worry anymore, start from the first one outside
        # the right coverage of it and continue with the corresponding house number
        location = x[i] + k
        while i < len(x) and x[i] <= location:
            i += 1
    return count