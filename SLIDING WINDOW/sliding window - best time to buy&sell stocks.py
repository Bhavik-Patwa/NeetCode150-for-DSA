# Problem 5.1 - Best Time to Buy and Sell Stock
# Given prices of a stock over days, return the maximum profit from a single buy-sell transaction (buy before you sell).


# ---------------------------------------------------------------------------------------------------------------------------------------
# 1. Brute Force
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Try every possible pair of days and calculate the profit; return the maximum.
# Time  : O(n²)         {nested loop over all pairs}
# Space : O(1)
class Solution1:
    def maxProfit(self, prices):
        res = 0
        for i in range(len(prices)):                    # For each buy
            buy = prices[i]
            for j in range(i + 1, len(prices)):         # Checking all possible sell days
                sell = prices[j]
                res = max(res, sell - buy)              # Updating max profit if better
        return res                                      # Highest profit -> best day to buy and sell the stock


# ---------------------------------------------------------------------------------------------------------------------------------------
# 2. Two Pointers (Sliding Window)
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Use two pointers : buy at l, sell at r and update pointers as you find better opportunities.
# Time  : O(n)         {single pass through list}
# Space : O(1)
class Solution2:
    def maxProfit(self, prices):                    # Tracking and comparing the cheapest buy with following sell prices
        l, r = 0, 1                                 # l = buy : tending to cheapest buy, r = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:               # Profitable transaction
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r                               # Updating to cheapest buy seen
            r += 1                                  # Always moving sell pointer forward
        return maxP


# ---------------------------------------------------------------------------------------------------------------------------------------
# 3. Dynamic Programming 
# ---------------------------------------------------------------------------------------------------------------------------------------
# Idea  : Track the minimum price seen so far and calculate the profit if sold today; update max profit accordingly.
# Time  : O(n)         {single pass through list}
# Space : O(1)
class Solution3:
    def maxProfit(self, prices):
        maxP = 0
        minBuy = prices[0]                      # Lowest price so far

        for sell in prices:
            maxP = max(maxP, sell - minBuy)     # Trying to sell today, compared with the minimum price seen so far
            minBuy = min(minBuy, sell)          # Updating minimum buying price
        return maxP



def main():
    prices = [10, 5, 1, 6, 7, 1]
    print(prices)
    print(Solution1().maxProfit(prices))
    print(Solution2().maxProfit(prices))
    print(Solution3().maxProfit(prices))


if __name__ == '__main__':
    main()