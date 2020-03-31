import bisect


def num_match_subseq(S, words):
    # to make sure the characters are found in sequence, have to ensure that the later matched character has bigger index
    count = 0
    dic = {}
    for i in range(len(S)):
        if S[i] in dic:
            dic[S[i]].append(i)
        else:
            dic[S[i]] = [i]

    for word in words:
        if len(word) > len(S) or len(word) == 0:
            continue
        prev = -1
        for c in word:
            if c not in dic:
                break
            # here means that found the character but need to know whether there is a match in dic has index after prev
            # and need to choose the first index after prev, use binary search
            # index is where prev should be to keep the ordered list in order, so index is the position of interest
            index = bisect.bisect(dic[c], prev)

            if index == len(dic[c]):
                # means no element in the array is bigger than prev, that prev needs to insert to the end, break
                break
            prev = dic[c][index]

        # this is important tip, just like while...else, can use else for for loop too, once reach end of for loop execute else
        else:
            count += 1
    return count
