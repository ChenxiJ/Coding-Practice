def sum_num_substring(n):
    dp = [int(n[0])] + [0] * (len(n) - 1)
    ans = int(n[0])
    # dp only stores sum of the substring that ends at i
    for i in range(1, len(n)):
        # don't forget every time bring the previous to 1 decimal higher by *10, needs to add n[i] once
        dp[i] = 10 * dp[i - 1] + int(n[i]) * i + int(n[i])
        ans += dp[i]
    return ans % (pow(10, 9) + 7)