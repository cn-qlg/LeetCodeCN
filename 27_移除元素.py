"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

解题思路：
与26题一样。
但是注意：元素的顺序可以改变
如果出现num=[1，2，3，5，4]，Val=4或者num=[4，1，2，3，5]，Val=4，都会出现一些不必要的操作。
所以可以通过将元素交换到后面的方法来避免这些操作。
"""


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        i = -1
        for j in range(len(nums)):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            # print(i, j, nums)
        return i + 1

    def removeElement2(self, nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i]= nums[j]
                j -=1
            else:
                i +=1
        return i


if __name__ == "__main__":
    print(Solution().removeElement([1], 1))
    print(Solution().removeElement2([1], 1))
    print(Solution().removeElement([1, 1], 1))
    print(Solution().removeElement2([1, 1], 1))
    print(Solution().removeElement([1, 1], 2))
    print(Solution().removeElement2([1, 1], 2))
    print(Solution().removeElement([3], 2))
    print(Solution().removeElement2([3], 2))
    print(Solution().removeElement([3, 2, 2, 3], 3))
    print(Solution().removeElement2([3, 2, 2, 3], 3))
    print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    print(Solution().removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2))
