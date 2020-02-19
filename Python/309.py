# 309. Best Time to Buy and Sell Stock with Cooldown

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
from typing import List


class Solution:
    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        hold = [float("-inf") for _ in range(n + 1)]
        sell = [0 for _ in range(n + 1)]
        wait = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            today_price = prices[i - 1]
            # just hold or buy some stock
            hold[i] = max(hold[i - 1], wait[i - 1] - today_price)
            # just wait or sell some stock from sell state into wait
            wait[i] = max(wait[i - 1], sell[i - 1])
            # sell can only changed from hold, sell some stock
            sell[i] = hold[i - 1] + today_price
        return max(wait[n], sell[n])

    def maxProfit(self, prices: List[int]) -> int:
        hold = float("-inf")
        sell = 0
        wait = 0
        for price in prices:
            hold = max(hold, wait - price)
            origin_sell = sell
            sell = hold + price
            wait = max(wait, origin_sell)
        return max(wait, sell)


if __name__ == '__main__':
    from util import Test
    t = Test(Solution().maxProfit)
    t.equal(3, [1, 2, 3, 0, 2])
    t.equal(0, [])
    t.equal(1, [0, 1])
    t.equal(3, [1, 2, 4])
