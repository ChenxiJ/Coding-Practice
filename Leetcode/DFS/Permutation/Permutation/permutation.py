def permute(nums):
    ans = []
    used = [False] * len(nums)

    def dfs(cur):
        if len(cur) == len(nums):
            ans.append(cur.copy())
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            cur.append(nums[i])
            used[i] = True
            dfs(cur)
            cur.pop()
            used[i] = False

    dfs([])
    return ans
