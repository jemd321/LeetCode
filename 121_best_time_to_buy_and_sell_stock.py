class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices):
        if not prices:
            return 0
        lowest = prices[0]
        best_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest
            if profit > best_profit:
                best_profit = profit
        return best_profit


class Test:
    test = BestTimeToBuyAndSellStock()
    print(test.maxProfit([7, 1, 5, 3, 6, 4]))
    print(test.maxProfit([7, 6, 4, 3, 1]))
    print(test.maxProfit([0]))
    print(test.maxProfit([-1, -2, -3]))
    print(test.maxProfit([-3, -2, -1]))