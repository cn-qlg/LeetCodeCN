#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#

# @lc code=start


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = nums[0]
        n = len(nums)
        for i in range(1, n):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            if nums[i] > m:
                m = nums[i]
        return m


# @lc code=end
if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(Solution().maxSubArray([1]))
    print(Solution().maxSubArray([5, 4, -1, 7, 8]))
