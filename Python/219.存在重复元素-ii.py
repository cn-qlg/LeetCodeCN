#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
"""解题思路
1. 先用字典存储每个数字的下标，然后从有多个下标的数字里，找是否有符合条件的
2. 优化，如果下标p,q,r下标所在的元素相等，且p<q<r，如果满足abs(p,r)<=k,则一定有abs(q,r)<=k。
    所以，基本上只需要判断后两个下标是否符合就行了。
"""
from typing import List
# @lc code=start


class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    #     d = dict()
    #     for i, n in enumerate(nums):
    #         if n in d:
    #             d[n].append(i)
    #         else:
    #             d[n] = [i]
    #     # print(d)
    #     for _, indexs in d.items():
    #         if len(indexs) > 1:
    #             if self.search(indexs, k):
    #                 return True

    #     return False

    # def search(self, indexs: List[int], k):
    #     l = len(indexs)

    #     for i in range(l):
    #         for j in range(i+1, l):
    #             if indexs[j] - indexs[i] <= k:
    #                 return True
    #     return False


    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, n in enumerate(nums):
            if n in d:
                if i - d[n] <= k:
                    return True
            d[n] = i
        return False
    


# @lc code=end
print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
