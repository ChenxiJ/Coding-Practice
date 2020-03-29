def num_trees(n):
    dp = [1, 1] + [0] * (n - 1)
    for i in range(1, n + 1):
        dp[i] = sum(dp[k] * dp[i-k-1] for k in range(i))
    return dp[-1]