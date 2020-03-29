def max_profit_cool_down(prices):
    if len(prices) < 1:
        return 0
    # dp_0 tracks the max_profit at end of ith day when no stock in hand
    # dp_1 ... one stock in hand
    dp_0 = [0] * len(prices)
    dp_1 = [-prices[0]] + [0] * (len(prices) - 1)

    for i in range(1, len(prices)):
        # ith day, rest or sold one stock, fee only happens either buy or sell
        dp_0[i] = max(dp_0[i - 1], dp_1[i - 1] + prices[i])
        # ith day, rest or bought one stock, but previous day cannot buy
        if i == 1:
            dp_1[i] = max(dp_1[0], -prices[1])
        dp_1[i] = max(dp_1[i - 1], dp_0[i - 2] - prices[i])
    return dp_0[-1]