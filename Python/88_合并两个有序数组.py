"""
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
首先由于是有序数组，而且必须原地修改。
一种方式是，直接把nums1拷贝出来即为nums_copy，然后两个指针头分别指向nums_copy和nums2。然后分别比较两个数组当前数值大小，并把小的赋值到num1中。同时移位下标。
但是这种方式需要赋值一次，所以，可以直接从后往前比较。大的放在最后面。
第三种就比较骚了，直接利用高级语言的特性，先相加，再排序。
"""


class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m -1
        j = n - 1
        t = m + n - 1
        while i >=0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[t] = nums1[i]
                i -=1
            else:
                nums1[t] = nums2[j]
                j -=1
            t -= 1
        if j >=0:
            nums1[:j+1] = nums2[:j+1]
        print(nums1)
    
    def merge2(self, nums1, m, nums2, n):
        i = 0
        j = 0

        nums_copy = nums1[:]
        while i <m and j < n:
            if nums_copy[i]< nums2[j]:
                nums1[i + j] = nums_copy[i]
                i +=1
            else:
                nums1[i + j] = nums2[j]
                j +=1
        if i< m:
            nums1[i + j:] = nums_copy[i:m]
        else:
            nums1[i + j:] = nums2[j:]
        print(nums1)
    
    def merge3(self, nums1, m, nums2, n):
        nums1[:] =  sorted(nums1[:m] + nums2)
        print(nums1)
        





if __name__ == "__main__":
    print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(Solution().merge2([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(Solution().merge3([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(Solution().merge([2,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge2([2,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge3([2,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge([4,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge2([4,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge3([4,5,6,0,0,0], 3, [1,2,3], 3))
    print(Solution().merge([1,2,3,0,0,0], 3, [4,5,6], 3))
    print(Solution().merge2([1,2,3,0,0,0], 3, [4,5,6], 3))
    print(Solution().merge3([1,2,3,0,0,0], 3, [4,5,6], 3))
