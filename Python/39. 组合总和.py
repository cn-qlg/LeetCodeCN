from typing import List

"""
解题思路：
使用dfs，深度遍历即可，但是需要注意题目中没有说明数据是有序的，所以需要先排序。
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()
        self.dfs(candidates, target, [])
        return self.result

    
    def dfs(self, candidates: List[int], target: int, current: List[int]):        
        s = sum(current)
        if s == target:
            self.result.append(current)
            return
        for idx, c in enumerate(candidates):
            if target < c+ s:
                return
            else:
                t = current.copy()
                t.append(c)
                self.dfs(candidates[idx:], target, t)




if __name__ == "__main__":
    print(Solution().combinationSum([2,3,5], 7))
    print(Solution().combinationSum([2,3,5], 8))
    print(Solution().combinationSum([8,7,4,3], 11))

