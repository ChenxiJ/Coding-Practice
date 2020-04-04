# this will time out, O(n^2)
def subarray_sum1(nums, k):
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = dp[i][j - 1] + nums[j]
            if dp[i][j] == k:
                count += 1
    return count


# use hash to store the count of prefix sum, O(n)
def subarray_sum(nums, k):
    # initialize the dic so at the first element prefix is 0
    dic = {0: 1}
    cur_sum = 0
    count = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        # sum 0...j is sum-k so sum j+1...i is k
        if cur_sum - k in dic:
            count += dic[cur_sum - k]
        # need to add the prefix to dic only after the current count because it is counting the prefix count before current
        dic[cur_sum] = dic.get(cur_sum, 0) + 1

    return count
