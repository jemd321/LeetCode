class BestTimeToBuyAndSellStock2:
    def maxProfit(self, prices):
        if not prices:
            return 0
        prev = prices[0]
        total_profit = 0
        for i, p in enumerate(prices):
            if p > prev:
                total_profit += (p - prev)
            prev = p
        return total_profit


class Test:
    test = BestTimeToBuyAndSellStock2()
    print(test.maxProfit([7, 1, 5, 3, 6, 4]))
    print(test.maxProfit([7, 6, 4, 3, 1]))
    print(test.maxProfit([0]))
    print(test.maxProfit([-1, -2, -3]))
    print(test.maxProfit([-3, -2, -1]))