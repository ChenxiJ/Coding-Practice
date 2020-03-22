def coin_change_ways(n, c):
    dp = [1] + [0] * n

    for i in range(1, 1 + n):
        for j in c:
            if j <= i:
                dp[i] = dp[i - j] + dp[i]
    return dp[-1]