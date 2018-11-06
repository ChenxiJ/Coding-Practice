def abbreviation(a, b):
    lena = len(a)
    lenb = len(b)
    dp = [[0] * (lena + 1) for i in range(lenb + 1)]
    if a[0].isupper() and a[0] != b[0]:
        return 'NO'
    else:
        dp[0][0] = 1

    for indexa in range(1, lena + 1):
        for indexb in range(lenb + 1):
            if a[indexa - 1].islower():
                dp[indexb][indexa] = dp[indexb][indexa - 1]
            if indexb > 0 and dp[indexb - 1][indexa - 1] == 1 and a[indexa - 1].upper() == b[indexb - 1]:
                        dp[indexb][indexa] = 1

    if dp[-1][-1] == 1:
        return 'YES'
    else:
        return 'NO'