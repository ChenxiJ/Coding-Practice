def equalStacks(h1, h2, h3):
    stack1, stack2, stack3 = [], [], []
    sum1, sum2, sum3 = 0, 0, 0
    for i in range(len(h1)-1, -1, -1):
        sum1 += h1[i]
        stack1.append(sum1)
    for i in range(len(h2)-1, -1, -1):
        sum2 += h2[i]
        stack2.append(sum2)
    for i in range(len(h3)-1, -1, -1):
        sum3 += h3[i]
        stack3.append(sum3)
    while len(stack1) > 0 and len(stack2) > 0 and len(stack3) > 0:
        if stack1[-1] == stack2[-1] == stack3[-1]:
            return stack1[-1]
        else:
            highest = max(stack1[-1], stack2[-1], stack3[-1])
            if highest == stack1[-1]:
                stack1.pop()
            if highest == stack2[-1]:
                stack2.pop()
            if highest == stack3[-1]:
                stack3.pop()
    return 0