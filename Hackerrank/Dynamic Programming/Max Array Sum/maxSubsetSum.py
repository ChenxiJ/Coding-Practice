def maxSubsetSum(arr):
    dp = [0] * len(arr)
    # base cases
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    # for any further entries, max sum is either the new element in the array, the sum so far, 
    # or the sum of the previous sum and the new element
    for i in range(2,len(arr)):
        dp[i] = max(dp[i - 1], arr[i])
        dp[i] = max(dp[i], dp[i - 2] + arr[i])
    return dp[-1]