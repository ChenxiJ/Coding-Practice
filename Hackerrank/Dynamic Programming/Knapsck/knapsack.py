def unbounded_knapsack(k, arr):
    for q in range(k + 1, 0, -1):
        dp = [1] + [0] * (q - 1)
        for i in range(1, q):
            for j in arr:
                if j <= i:
                    dp[i] = dp[i - j] + dp[i]
        if dp[-1] > 0:
            return q - 1
    return 0
