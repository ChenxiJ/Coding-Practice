def combination_sum2(candidates, target):
    cur = []
    ans = []
    # sort the candidate so when iterate from the start, once the value is larger than the target can skip more  checking
    candidates.sort()

    def dfs(target_left, s):
        if target_left == 0:
            ans.append(cur.copy())
            return
        for i in range(s, len(candidates)):
            # make use of the sorted candidate
            if candidates[i] > target_left:
                break
            # this is to ensure in the same level of recursion won't consider starting from the same value
            if i > s and candidates[i] == candidates[i - 1]:
                continue
            cur.append(candidates[i])
            dfs(target_left - candidates[i], i + 1)
            # cur is the 'path' so far, if previous path dead end, backtrack to last state and continue, so when looking for
            # solution with [2,2,2] then next 2 already exceeding the target_left 1, so break the dfs and cur pops the last
            # element out, cur = [2,2] then start exploring 3
            cur.pop()

    dfs(target, 0)
    return ans
