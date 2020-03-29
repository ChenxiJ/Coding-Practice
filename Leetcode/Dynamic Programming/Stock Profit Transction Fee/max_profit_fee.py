def max_profit_transaction_fee(prices, fee):
    if len(prices) < 1:
        return 0
    # dp_0 tracks the max_profit at end of ith day when no stock in hand
    # dp_1 ... one stock in hand
    dp_0 = [0] * len(prices)
    # if hold on stock at the end of the first day, profit will be negative not 0, important to set the base condition correctly!
    dp_1 = [-prices[0] - fee] + [0] * (len(prices) - 1)
    for i in range(1, len(prices)):
        # ith day, rest or sold one stock, fee only happens either buy or sell
        dp_0[i] = max(dp_0[i - 1], dp_1[i - 1] + prices[i])
        # ith day, rest or bought one stock
        dp_1[i] = max(dp_1[i - 1], dp_0[i - 1] - prices[i] - fee)

    return dp_0[-1]
