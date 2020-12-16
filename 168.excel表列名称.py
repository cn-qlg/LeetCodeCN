#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        values = {
            1:	"A",
            2:	"B",
            3:	"C",
            4:	"D",
            5:	"E",
            6:	"F",
            7:	"G",
            8:	"H",
            9:	"I",
            10:	"J",
            11:	"K",
            12:	"L",
            13:	"M",
            14:	"N",
            15:	"O",
            16:	"P",
            17:	"Q",
            18:	"R",
            19:	"S",
            20:	"T",
            21:	"U",
            22:	"V",
            23:	"W",
            24:	"X",
            25:	"Y",
            26:	"Z"
        }
        name = []
        while n > 0:
            n, mod = divmod(n, 26)
            if mod == 0:
                n -= 1
                mod = 26

            name.append(values[mod])
        return "".join(name[::-1])


# @lc code=end
print(1, "A", Solution().convertToTitle(1))
print(26, "Z", Solution().convertToTitle(26))
print(28, "AB", Solution().convertToTitle(28))
print(52, "AZ", Solution().convertToTitle(52))
print(78, "BZ", Solution().convertToTitle(78))
print(701, "ZY", Solution().convertToTitle(701))
print(702, "ZZ", Solution().convertToTitle(702))
print(703, "AAA", Solution().convertToTitle(703))
print(704, "AAB", Solution().convertToTitle(704))
print(728, "AAZ", Solution().convertToTitle(728))
