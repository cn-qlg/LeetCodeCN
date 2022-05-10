#
# @lc app=leetcode.cn id=228 lang=python
#
# [228] 汇总区间
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        i = 0
        length = len(nums)
        while i < length:
            p = nums[i]
            for j in range(length-i+1):
                if i + j >= length or (j + p) != nums[i+j]:
                    break

            if nums[i+j-1] == p:
                res.append(str(p))
                i += 1
            else:
                res.append("{0}->{1}".format(p, nums[i+j-1]))
                i = i + j

        return res


# @lc code=end
print(Solution().summaryRanges([1, 3]))
print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
print(Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]))
