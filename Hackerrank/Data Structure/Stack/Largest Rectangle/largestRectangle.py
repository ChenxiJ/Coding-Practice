def largest_rectangle(h):
    s = []
    ans = len(h)
    h.append(0)

    for i in range(len(h)):
        left_index = i
        while len(s) > 0 and h[i] <= s[-1][1]:
            # when new building is shorter or equal to the one before, means can merge
            # start popping out until the new height bigger than the top of the stack
            last = s.pop()
            left_index = last[0]

            # since only ascending order height are added to the stack, all the later pooped out one can merge right to
            # the first popped out one, max can be the popped out height * distance from the highest (first pooped )
            ans = max(ans, last[1] * (i - last[0]))

            # or max is the lower height after the peak but merged as left as possible, length is one more than the 
            # previous one since the last shorter h[i] is included, merge left (until h[i] > top height in stack)
            ans = max(ans, h[i] * (i + 1 - last[0]))
            
        # when new height higher, put the index and building height in a stack
        s.append((left_index, h[i]))
    return ans
