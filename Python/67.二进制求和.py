#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2))[2:])

    # def addBinary1(self, a: str, b: str) -> str:
    #     if not a:
    #         return b
    #     if not b:
    #         return a
    #     l1 = len(a) - 1
    #     l2 = len(b) - 1
    #     carry = 0
    #     result = []
    #     while l1 >= 0 and l2 >= 0:
    #         c1 = int(a[l1])
    #         c2 = int(b[l2])
    #         v = (c1 + c2 + carry) % 2
    #         carry = (c1 + c2 + carry) // 2
    #         result.append(v)
    #         l1 -= 1
    #         l2 -= 1
    #     if l1 >= 0:
    #         while l1 >= 0:
    #             c = int(a[l1])
    #             v = (c + carry) % 2
    #             carry = (c + carry) // 2
    #             result.append(v)
    #             l1 -= 1
    #     if l2 >= 0:
    #         while l2 >= 0:
    #             c = int(b[l2])
    #             v = (c + carry) % 2
    #             carry = (c + carry) // 2
    #             result.append(v)
    #             l2 -= 1
    #     if carry > 0:
    #         result.append(1)
    #     return "".join([str(v) for v in result[::-1]])


# @lc code=end
print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1", "111"))
print(Solution().addBinary("11", "10"))
print(Solution().addBinary("11", "11"))
print(Solution().addBinary("1010", "1011"))
