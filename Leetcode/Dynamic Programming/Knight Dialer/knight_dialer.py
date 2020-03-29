# the key point is to realize the number sequences of length N starting with digit d1, is the sum of the number of sequences
# of length N-1 starting with digits that d1 can go from


def knight_dialer(N):
    next_digit = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3],
                  9: [2, 4]}
    dp = [[0] * 10 for _ in range(N)]
    for j in range(10):
        dp[0][j] = 1
    for i in range(1, N):
        for j in range(10):
            if j in next_digit:
                digits = next_digit[j]
                dp[i][j] = sum(dp[i - 1][digit] for digit in digits)
    return sum(dp[-1])


# since a row in dp only using last row, can save space by using only two arrays of length 10
def knight_dialer_less_space(N):
    if N == 1:
        return 10
    next_digit = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3],
                  9: [2, 4]}
    dp_prev = [1] * 10
    dp = [0] * 10

    for i in range(1, N):
        for j in range(10):
            if j in next_digit:
                digits = next_digit[j]
                dp[j] = sum(dp_prev[digit] for digit in digits)

        # this is important, otherwise last line the dp_prev is updating with dp, sum will go wrong
        dp_prev = dp.copy()
    return sum(dp)
