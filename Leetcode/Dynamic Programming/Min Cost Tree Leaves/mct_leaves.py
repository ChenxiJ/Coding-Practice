import sys


def mct_from_leaves(arr):
    # dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + max(arr[i...k]) * max(arr[k+1...j]))
    dp = [[0] * len(arr) for _ in range(len(arr))]

    for i in range(len(arr) - 2, -1, -1):
        for j in range(i + 1, len(arr)):
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                # problem in here is that the dp used in updating current dp[i][j] is not necessarily updated themselves
                # !!! dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j+1]))
                # way to solve is to start the front pointer from the back so start with very small range that dp is calculated
                # i every time move from back to front one and j move from i to the back each time increasing the gap
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))

    return dp[0][-1]
