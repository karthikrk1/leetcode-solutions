"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

"""

class Solution:
    def max_profit(self, prices):
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


def main():
    sol = Solution()
    assert sol.max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert sol.max_profit([1, 2, 3, 4, 5]) == 4
    assert sol.max_profit([5, 4, 3, 2, 1]) == 0


if __name__ == '__main__':
    main()