def permute_unique(nums):
    ans = []
    used = [False] * len(nums)
    # important to prevent duplicate in answer
    nums.sort()

    def dfs(cur):
        if len(cur) == len(nums):
            ans.append(cur.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            # this is so smart, same number can only be used once at each depth, last same one not used means they can be
            # used later at this same depth. need to sort array for this purpose!!!!!
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            cur.append(nums[i])
            used[i] = True
            dfs(cur)
            cur.pop()
            used[i] = False

    dfs([])
    return ans
