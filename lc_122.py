# lc_122.py
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        max_so_far = 0
        for i in range(1, len(prices)):
            cur_max += prices[i]-prices[i-1]
            cur_max = max(0, cur_max)
            max_so_far = max(max_so_far, cur_max)
        return max_so_far
    