class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        maxPrice = 0

        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxPrice:
                maxPrice = p - minPrice

        return maxPrice
