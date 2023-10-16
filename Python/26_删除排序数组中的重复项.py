"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 

示例 1:

给定数组 nums = [1,1,2], 

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
 

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

解题思路：
首先题目说了是排序数组，那么利用两个指针，一次遍历即可完成。
另外似乎不需要删除也行……
比如[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
step1: i=0, j=1 判断nums[i]和nums[j]的大小。nums[i]=nums[j],直接跳过。                 数组不变[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
step2: i=0, j=2 判断nums[i]和nums[j]的大小。nums[i]<nums[j]。i+1,并赋值nums[i]=nums[j].数组变为[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
step3: i=1, j=3 判断nums[i]和nums[j]的大小。nums[i]=nums[j],直接跳过。                 数组不变[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
step4: i=1, j=4 判断nums[i]和nums[j]的大小。nums[i]=nums[j],直接跳过。                 数组不变[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
step5: i=1, j=5 判断nums[i]和nums[j]的大小。nums[i]<nums[j]。i+1,并赋值nums[i]=nums[j].数组变为[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
以此类推，这样一轮遍历下来，保证nums[0]~nums[i]的都是不重复的。
"""


class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        length = len(nums)
        while j < length:
            if nums[i] < nums[j]:
                i +=1
                nums[i] = nums[j]
            if nums[i] == nums[j]:
                pass
            j += 1
        # print("before,", nums)
        # for t in range(i+1, length):
        #     # print(nums)
        #     del [nums[i+1]]
        # print("after", nums)
        return i + 1

                    

if __name__ == "__main__":
    print(Solution().removeDuplicates([1]))
    print(Solution().removeDuplicates([1, 1]))
    print(Solution().removeDuplicates([1, 2]))
    print(Solution().removeDuplicates([1, 1, 2]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

