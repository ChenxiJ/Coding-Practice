# the idea is to tackle two stacks from different side, one from the back, removing 1 at a time and adding the other
# stack from the start until sum exceeds, while keep tracking of the running sum of the total removal at all times

def two_stacks(x, a, b):
    stack_a, stack_b = [], []
    sum_a, sum_b = 0, 0
    for i in a:
        sum_a += i
        if sum_a <= x:
            stack_a.append(sum_a)
        else:
            break

    for i in b:
        sum_b += i
        if sum_b <= x:
            stack_b.append(sum_b)
        else:
            break

    best_num = max(len(stack_a), len(stack_b))
    index_b = 0
    for i in range(len(stack_a) - 1, -1, -1):

        while index_b < len(stack_b) and stack_a[i] + stack_b[index_b] <= x:
            index_b += 1
            best_num = max(best_num, i + 1 + index_b)
    return best_num