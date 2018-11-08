def nextGreaterValue(arr):
    res = [-1] * len(arr)
    # put index and value to stack
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0 or arr[i] < stack[-1][1]:
            stack.append((i, arr[i]))
        else:
            while len(stack) != 0 and arr[i] > stack[-1][1]:
                last = stack.pop()
                res[last[0]] = i - last[0]
            stack.append((i, arr[i]))
    return res