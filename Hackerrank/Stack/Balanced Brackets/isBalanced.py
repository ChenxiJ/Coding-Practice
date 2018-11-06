def isBalanced(s):
    if len(s)%2 == 1:
        return 'NO'
    stack = []
    toPush = ['{', '[', '(']
    match = {'{':'}', '[':']', '(':')'}
    for i in s:
        if i in toPush:
            stack.append(match[i])
        else:
            # pay attention to the order. remember the case where ')' appears first
            if len(stack) == 0 or i != stack[-1]:
                return 'NO'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'