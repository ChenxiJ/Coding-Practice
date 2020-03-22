import sys


def min_coins(coin, value):
    # dp = [[0 for x in range(value + 1)] for x in range(len(coin) + 1)]
    dp = [[0] * (value + 1) for x in range(len(coin) + 1)]
    # rows are set of the i smallest valued coins, starting from 1
    # columns j are value to be paid, starting from 0 to value

    dp[0] = [sys.maxsize] * (value + 1)
    for i in range(1, len(coin) + 1):
        for j in range(1, value + 1):
            if j < coin[i - 1]:
                # means previous coin already covered new value
                dp[i][j] = dp[i - 1][j]
            else:
                # either use the highest value coin or not
                dp[i][j] = min(1 + dp[i][j - coin[i - 1]], dp[i - 1][j])
    return dp[-1][-1]


# here can optimize space since only using previous row, no need to save all rows, only need 1-d array instead of matrix

def min_coin_opt(coin, value):
    dp = [0] + [sys.maxsize] * value
    for i in range(1, len(coin) + 1):
        for j in range(coin[i - 1], value + 1):
            dp[j] = min(1 + dp[j - coin[i - 1]], dp[j])
    return dp[-1]
