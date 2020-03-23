# key of the problem is to start from the back. As long as the price is the highest so far,
# all the shares purchased previously (which is lower then current max) will gain profit, so just buy it.
# If there is a new higher peak, then reset the peak and re-do it


def stock_maximize(prices):
    max_temp = prices[-1]
    profit = 0
    for i in range(len(prices) - 2, -1, -1):

        if prices[i] <= max_temp:
            profit += max_temp - prices[i]

        max_temp = max(max_temp, prices[i])
    return profit
