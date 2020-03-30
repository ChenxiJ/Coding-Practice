def find_target_sum_ways1(nums, S):
    # this is like dfs get all the possible combinations, will time out
    dp_prev = [0]
    for i in range(len(nums)):
        dp = []
        for s in dp_prev:
            dp.append(s + nums[i])
            dp.append(s - nums[i])
        dp_prev = dp.copy()

    count = 0
    for i in dp:
        if i == S:
            count += 1
    return count


def find_target_sum_ways(nums, S):
    # important to see the sub-problem: dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
    # dp = [[] * (2 * nums_sum + 1) for i in range(len(nums)+1)]
    # in the end only using last row so need just two arrays

    nums_sum = sum(nums)
    dp_prev = [0] * (2 * nums_sum + 1)
    # index shift from -nums_sum...nums_sum to 0...2 * nums_sum, so index nums_sum means sum=0
    # there is one way to use 0 elements to achieve sum 0
    dp_prev[nums_sum] = 1
    for i in range(len(nums)):
        dp = [0] * (2 * nums_sum + 1)
        for j in range(2 * nums_sum + 1):
            if 0 <= j - nums[i] <= 2 * nums_sum and 0 <= j + nums[i] <= 2 * nums_sum:
                dp[j] = dp_prev[j - nums[i]] + dp_prev[j + nums[i]]
            elif 0 <= j - nums[i] <= 2 * nums_sum:
                dp[j] = dp_prev[j - nums[i]]
            elif 0 <= j + nums[i] <= 2 * nums_sum:
                dp[j] = dp_prev[j + nums[i]]
        dp_prev = dp.copy()
    return dp[S + nums_sum] if 0 <= S + nums_sum <= 2 * nums_sum else 0
