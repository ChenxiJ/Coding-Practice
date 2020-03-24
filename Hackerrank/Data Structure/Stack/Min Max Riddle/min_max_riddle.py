def riddle(arr):
    # now put in dic {value: longest_window}
    dic = {}
    stack = []
    # to make sure all the element will pop out in the stack (ext element is smaller), add 0 to the end of the array
    arr.append(0)

    for i in range(len(arr)):
        index = i
        # pops out when new element is smaller, when there is popping out, append [smallest_value, from_this_index]
        while len(stack) > 0 and arr[i] <= stack[-1][0]:

            popped = stack.pop()
            if arr[i] not in dic:
                dic[arr[i]] = 1
            if popped[0] not in dic:
                dic[popped[0]] = 1
                # since the new one is smaller than the top of the stack, it must be at least smallest in a window
                # that is the distance_new_element_to_that_top + 1, and the popped out value is at least the smallest
                # for a window just before the new minimal appears, which is just distance_new_element_to_that_top
            dic[arr[i]] = max(dic[arr[i]], i - popped[1] + 1)
            dic[popped[0]] = max(dic[popped[0]], i - popped[1])

            # now when append the new smallest value to the stack, we take the index of the last element that was popped
            # so that the new minimal is at least the minimal from that index, then in the future, new minimal just need
            # to calculate the distance to the current minimal+1 + window length current index covers

            index = popped[1]
        stack.append([arr[i], index])

    del dic[0]

    # for when the max_win_length same, only keep the key that is maximum
    max_dic = {}
    for key, val in dic.items():
        if val not in max_dic:
            max_dic[val] = key
        else:
            max_dic[val] = max(max_dic[val], key)

    # from the back is important, don't get we added 0 to the end of the arr at the beginning!
    # mistake here is that not all the values in the dictionary is needed!!! can happen at the front of the array,
    # for length 8, max_value = 100, but at the back of the array, for length 10, max_value = 200, then of course the
    # length = 8 case is covered by the max_value = 200. Only update is the value in dic is actually bigger
    ans = [max_dic[len(arr) - 1]]
    for i in range(len(arr) - 2, 0, -1):
        if i in max_dic and max_dic[i] > ans[-1]:
            ans.append(max_dic[i])
        else:
            ans.append(ans[-1])
    ans.reverse()
    return ans
