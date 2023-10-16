"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

分析：
大体上两种思路：
1. 就是暴力穷举法，一个一个遍历
2. 利用dict（或者称为hashmap），由于题目说了，只会有一种答案,那么target - nums[i]也必定在dict(nums)里面
"""


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums[i + 1:]):
                if v1 + v2 == target:
                    return [i, j+i+1]

    def twoSum2(self, nums, target):
        hashmap = dict()
        for index, num in enumerate(nums):
            hashmap[num] = index
        for index, num in enumerate(nums):
            if target - num in hashmap:
                another_index = hashmap[target - num]
                if index != another_index:
                    return [index, hashmap[target - num]]

    def twoSum3(self, nums, target):
        hashmap = dict()
        for index, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target-num], index]
            hashmap[num] = index


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
    print(Solution().twoSum2([2, 7, 11, 15], 9))
    print(Solution().twoSum3([2, 7, 11, 15], 9))
    print(Solution().twoSum([2, 7, 11, 15], 17))
    print(Solution().twoSum2([2, 7, 11, 15], 17))
    print(Solution().twoSum3([2, 7, 11, 15], 17))
    print(Solution().twoSum([2, 7, 11, 15], 26))
    print(Solution().twoSum2([2, 7, 11, 15], 26))
    print(Solution().twoSum3([2, 7, 11, 15], 26))
    print(Solution().twoSum([2, 5, 5, 11], 10))
    print(Solution().twoSum2([2, 5, 5, 11], 10))
    print(Solution().twoSum3([2, 5, 5, 11], 10))
    print(Solution().twoSum([3, 2, 4], 6))
    print(Solution().twoSum2([3, 2, 4], 6))
    print(Solution().twoSum3([3, 2, 4], 6))
    print(Solution().twoSum([2, 3, 4], 6))
    print(Solution().twoSum2([2, 3, 4], 6))
    print(Solution().twoSum3([2, 3, 4], 6))
