#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """方法一，与第7题类似，直接一次取出每一位的值，然后和反转后的值做比较。
        """
        if x <0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        r = 0
        v = x
        while v >0:
            q = v % 10
            v = v // 10
            r = r * 10 + q
        if r == x:
            return True
        # print(r, x)
        return False
    
    def isPalindrome(self, x: int) -> bool:
        """方法二，由于是判断回文。其实只需要取一半的数字即可，即取前半部分数字与后半部分数字反转后的结果相比。
        这样既可避免溢出问题，也可更快速进行判断。"""
        if x <0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        r = 0
        v = x
        while v >r:
            q = v % 10
            v = v // 10
            r = r * 10 + q
        if r == v or r//10 == v:
            return True
        print(r, x)
        return False
# @lc code=end
print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
print(Solution().isPalindrome(0))
print(Solution().isPalindrome(11))