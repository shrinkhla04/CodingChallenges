class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    """ for every value in the array we can check if this value is less than the min_price and find the profit 
    by considering that value of the array as SP and min_price as CP"""
        min_price = 10000000
        max_profit = 0
        for i in prices:
            if i < min_price:
                min_price = i
            if (i - min_price) > max_profit:
                max_profit = (i - min_price)
        return max_profit
# O(n) time and O(1) space
