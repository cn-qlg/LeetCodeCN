"""
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

 

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""
 

提示：

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] 和 str2[i] 为大写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-common-divisor-of-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
解题思路：
1. 笨方法，当做求最大公约数来处理
2. 看了解题思路，目前一脸懵逼。
看到一个最快解答：
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        if n1 == n2 and str1 != str2:
            return ""
        if n1 == n2 and str1 == str2:
            return str1
        if n1 < n2:
            return self.gcdOfStrings(str2[:n1], str2[n1:])
        if n1 > n2:
            return self.gcdOfStrings(str1[:n2], str1[n2:])
同样的代码人家20ms，我50ms……
"""


class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcdOfStrings(self, str1, str2):
        length1 = len(str1)
        length2 = len(str2)
        shortLength = min(length1, length2)
        longLength = max(length1, length2)
        if length1 > length2:
            return self.getLongestSubStr(str1, str2, shortLength, longLength)
        else:
            return self.getLongestSubStr(str2, str1, shortLength, longLength)

    def getLongestSubStr(self, longStr, shortStr, shortLength, longLength):
        gcdOfLength = shortLength
        while gcdOfLength > 0:
            if longLength % gcdOfLength == 0 and shortLength % gcdOfLength == 0:
                subStr = shortStr[0:gcdOfLength]
                if self.ifOnlyContainsOneSubStr(shortStr, subStr, shortLength, gcdOfLength) and self.ifOnlyContainsOneSubStr(longStr, subStr, longLength, gcdOfLength):
                    return subStr
            gcdOfLength -= 1
        return ""

    def ifOnlyContainsOneSubStr(self, sourceStr, subStr, sourceLength, subLength):
        cnt = sourceStr.count(subStr)
        if sourceLength / subLength == cnt:
            return True
        return False
    
    def gcdOfStrings2(self, str1, str2):
        l1 = len(str1)
        l2 = len(str2)
        if l1 == l2 and str1 == str2:
            return str1
        if l1 == l2 and str1 != str2:
            return ""
        if l1 > l2:
            return self.gcdOfStrings2(str1[l2:], str2)
        if l1 < l2:
            return self.gcdOfStrings2(str1, str2[l1:])


if __name__ == "__main__":
    print(Solution().gcdOfStrings("ABCABC", "ABC"))
    print(Solution().gcdOfStrings2("ABCABC", "ABC"))
    print(Solution().gcdOfStrings("ABABAB", "ABAB"))
    print(Solution().gcdOfStrings2("ABABAB", "ABAB"))
    print(Solution().gcdOfStrings("LEET", "CODE"))
    print(Solution().gcdOfStrings2("LEET", "CODE"))
