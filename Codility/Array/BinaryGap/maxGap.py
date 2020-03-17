def max_gap(N):
    binary = bin(N)[2:]
    prev_one = -1
    longest = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            first_one = i
            prev_one = i
            break
    for i in range(first_one+1, len(binary)):
        if binary[i] == '1':
            if (i - prev_one) > 1:
                longest = max(longest, i - prev_one - 1)
            prev_one = i
    return longest