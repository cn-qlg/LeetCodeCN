#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        max_profit = 0
        for p in prices[1:]:
            max_profit = max(max_profit, p - min)
            if p < min:
                min = p
        return max_profit

    # def maxProfit(self, prices):
    #     """
    #     :type prices: List[int]
    #     :rtype: int
    #     """
    #     """可能会超时
    #     """
    #     m = 0
    #     length = len(prices)
    #     for i in range(length-1):
    #         for j in range(i+1, length):
    #             m = max(prices[j]-prices[i], m)
    #     return m


# @lc code=end
if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
