def find_length(A, B):
    max_len = 0
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = 0
    return max_len
