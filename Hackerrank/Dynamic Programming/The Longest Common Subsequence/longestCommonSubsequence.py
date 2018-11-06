# Finding the common subsequenceit by backtracking exactly how the dp is built. From the last entry of dp, if row and column equals,
# then this value comes from its upper left cell + 1; if not, this value is from the bigger one of either its left or upper cell.
# Stick to one direction, for example left, then only when its upper cell is GREATER than its left cell, move up (if equal, moves left), 
# otherwise move left.

# about dp initialization, putting extra row and column of 0 before the real matrix extremely helpful!!
def longestCommonSubsequence(a, b):
    dp = [[0] * (len(a) + 1) for i in range(len(b) + 1)]
    ans = []
    # always remember there is one unit off between dp and a, b index! same when backtracking
    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            if b[i - 1] == a[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    length = dp[-1][-1]
    indexA = len(a) - 1
    indexB = len(b) - 1

    while length:
        if b[indexB] == a[indexA]:
            ans.append(b[indexB])
            length -= 1
            indexA -= 1
            indexB -= 1
        else:
            if dp[indexB][indexA + 1] > dp[indexB + 1][indexA]:
                indexB -= 1
            else:
                indexA -= 1
    ans.reverse()
    return ans