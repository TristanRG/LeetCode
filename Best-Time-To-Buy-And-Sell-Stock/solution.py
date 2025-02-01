class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 0
        profit = prices[0]
        for i in prices[:1]:
            minimum = min(minimum, i)
            profit = max(profit, i - minimum)
        
        print(profit)