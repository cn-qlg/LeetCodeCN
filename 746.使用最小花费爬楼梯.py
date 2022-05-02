#
# @lc app=leetcode.cn id=746 lang=python
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """解题思路
        f(i)表示达到第i层所需支付的总费用
        cost(i)表示第i层的费用
        f(i) = min(f(i-1) + cost(i-1), f(i-2) + cost(i-2))
        """
        s = list()
        s.append(0)
        s.append(0)
        length = len(cost)
        for i in range(2, length+1):
            s.append(min(s[i-1]+cost[i-1], s[i-2]+cost[i-2]))
        return s[-1]
# @lc code=end
print(Solution().minCostClimbingStairs([1,100]))
print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

