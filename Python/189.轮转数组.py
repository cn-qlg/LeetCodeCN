"""
解题思路：
1. 直接循环k次，每次移动一个，但是会超时。。
2. 将最后k个元素保存下来，再将0~n-k-1元素往后移，最后再将之前保存下来的k个元素复制到前部。
3. [1,2,3,4,5,6,7] k=2，先将整体翻转，得到[7,6,5,4,3,2,1],再将前k个翻转，得到[6,7,5,4,3,2,1],最后将k~-1进行翻转，得到[6,7,1,2,3,4,5]
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            c = nums[-1]
            for i in range(len(nums)-1,0, -1):
                nums[i]= nums[i-1]
            nums[0] = c
        
        print(nums)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        rights = nums[-k:]

        for i in range(length-k):
            nums[length-i-1] = nums[length-k-i-1]
        for i in range(k):
            nums[i] = rights[i]
        
        print(nums)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(0, length-1)
        reverse(0, k-1)
        reverse(k, length-1)
        
        print(nums)

if __name__ == "__main__":
    Solution().rotate([1,2,3,4,5,6,7], 3)
    Solution().rotate([-1,-100,3,99], 2)
    Solution().rotate([1,2,3],3)
    Solution().rotate([1],2)