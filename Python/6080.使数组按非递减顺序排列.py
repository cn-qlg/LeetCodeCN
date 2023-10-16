from sys import maxsize
from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        newNums = []
        step = 0
        while True:
            isDelete = False
            newNums = []
            newNums.append(nums[0])
            for i in range(1, len(nums)):
                if nums[i-1] <= nums[i]:
                    newNums.append(nums[i])
                else:
                    isDelete = True
            if not isDelete:
                break
            step += 1
            nums = newNums
            print(step, nums)
        return step
    # def totalSteps(self, nums: List[int]) -> int:
    #     maxSteps = 0
    #     pre,i, length = 0,1,len(nums)
    #     while i < length:
    #         if nums[i] >= nums[pre]:
    #             pre += 1
    #             i += 1
    #             continue
    #         j = i
    #         for j in range(i, length):
    #             if nums[j] >= nums[pre]:
    #                 break
    #         if (j-pre-1) > maxSteps:
    #             maxSteps = j-pre-1
    #         i = j + 1
    #         pre = j
    #     return maxSteps



if __name__ == "__main__":
    # print(Solution().totalSteps([5,3,4,4,7,3,6,11,8,5,11]))
    # print(Solution().totalSteps([5,3,4,4,7,3,6,1,1,11,8,5,11]))
    # print(Solution().totalSteps([5,3,4,4,4,4,7,3,6,11,8,5,11]))
    # print(Solution().totalSteps([4,5,7,7,13]))
    print(Solution().totalSteps([10,1,2,3,4,5,6,1,2]))

