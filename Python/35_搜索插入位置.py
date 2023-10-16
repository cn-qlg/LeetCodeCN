"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路：
由于是有序列表
最简单的方法，直接遍历一遍就好。
或者用二分法。
"""
class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        for i, v in enumerate(nums):
            if v >= target:
                return i
        return i + 1
    
    def searchInsert2(self, nums, target):
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        low, high = 0, len(nums) -1
        while low <= high:
            mid = (low + high) //2
            if nums[mid]> target:
                high = mid - 1   
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        if high < mid:
            return mid 
        return mid + 1


if __name__ == "__main__":
    print(Solution().searchInsert([1,3], 2))
    print(Solution().searchInsert2([1,3], 2))
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert2([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert2([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert2([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))
    print(Solution().searchInsert2([1,3,5,6], 0))