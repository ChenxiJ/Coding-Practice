def getPricesAndTradeInfo(datafeed):
    trades = {}
    prices = []
    dataEntry = str(datafeed).split("\n")
    for feed in dataEntry:
        data = feed.split("|")
        # save prices of a stock to an array
        if len(data) == 2:
            day = int(data[0])
            priceToday = int(data[1])
            if day == 0:
                prices.append(priceToday)
            else:
                while day > len(prices):
                    prices.append(prices[-1])
                else:
                    prices.append(priceToday)
        elif len(data) == 4:
            day = int(data[0])
            # save trades to a dictionary
            name = data[1]
            trades[day,name] = {"buyOrSell": data[2], "amount": int(data[3])}
    return prices,trades


def findPotentialInsiderTraders(datafeed):
    prices, trades = getPricesAndTradeInfo(datafeed)
    flaggedTrades = set()
    for dayAndTrade in trades:
        today = dayAndTrade[0]
        for day in range(today, min(today + 4, len(prices))):
            if dayAndTrade in flaggedTrades:
                continue
            transition = trades[dayAndTrade]

            if transition["buyOrSell"] == "BUY":
                a = transition["amount"]*(prices[day] - prices[today])
                if a > 500000:
                    flaggedTrades.add(dayAndTrade)
            else:
                a = transition["amount"]*(prices[today] - prices[day])
                if a > 500000:
                    flaggedTrades.add(dayAndTrade)
    flaggedTrades = sorted(list(flaggedTrades))

    return  list(map(lambda x: str(x[0]) + "|" + str(x[1]), flaggedTrades))