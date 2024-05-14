"""
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。

 

示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false
 

提示：

0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。

解题思路：
1. 针对s串的每一个字符，从t[index:]进行查找，如果找到，则更新index为当前字符在t中的下标+1，进行下一个字符查找。直到找不到，或者t字符串遍历完。
2. 双指针依次遍历。
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        for c in s:
            if index >= len(t):
                return False
            index = t.find(c,index)
            if index == -1:
                return False
            else:
                index += 1
        return True
            

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i,j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return m == i


if __name__ == "__main__":
    print(Solution().isSubsequence("abc", "ahbgdc"))
    print(Solution().isSubsequence("axc", "ahbgdc"))
    print(Solution().isSubsequence("axc", "a"))