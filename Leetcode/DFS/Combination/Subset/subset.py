# simple iteration
def subsets(nums):
    ans = [[]]
    for num in nums:
        # add latest num to all previous sub-arrays
        ans += [curr + [num] for curr in ans]
    return ans


# use dfs and backtracking, classic pattern
def subsets(nums):
    ans = []

    def dfs_combination(n, s, cur):
        if len(cur) == n:
            ans.append(cur.copy())
            return
        for i in range(s, len(nums)):
            cur.append(nums[i])
            dfs_combination(n, i + 1, cur)
            cur.pop()

    for i in range(len(nums) + 1):
        dfs_combination(i, 0, [])
    return ans
