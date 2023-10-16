#
# @lc app=leetcode.cn id=468 lang=python3
#
# [468] 验证IP地址
#
from typing import List
# @lc code=start
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        address = queryIP.split(".")
        if len(address) == 4:
            return self.validIPV4(address)
        address = queryIP.split(":")
        if len(address) == 8:
            return self.validIPV6(address)
        return "Neither"
    
    def validIPV4(self, address:List[str]):
        for seg in address:
            if len(seg) >= 2 and seg[0] == "0":
                return "Neither"
            if not seg.isdigit():
                return "Neither"
            num = int(seg)
            if num < 0 or num > 255:
                return "Neither"
        return "IPv4"
    
    def validIPV6(self, address:List[str]):
        nums = {"0","1","2","3","4","5","6","7","8","9"}
        alf = {"a","b","c","d","e","f","A","B","C","D","E","F"}
        for seg in address:
            if len(seg) < 1 or len(seg) > 4:
                return "Neither"
            for c in seg:
                if c not in nums and c not in alf:
                    return "Neither"
        return "IPv6"
            
# @lc code=end
print(Solution().validIPAddress("192.168.1.1")=="IPv4")
print(Solution().validIPAddress("192.168.1.0")=="IPv4")
print(Solution().validIPAddress("192.168.01.1")=="Neither")
print(Solution().validIPAddress("192.168.1.00")=="Neither")
print(Solution().validIPAddress("192.168@1.1")=="Neither")
print(Solution().validIPAddress("255.255.255.255")=="IPv4")
print(Solution().validIPAddress("256.256.256.256")=="Neither")
print(Solution().validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")=="IPv6")
print(Solution().validIPAddress("2001:db8:85a3:0:0:8A2E:0370:7334")=="IPv6")
print(Solution().validIPAddress("2001:0db8:85a3::8A2E:037j:7334")=="Neither")
print(Solution().validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334")=="Neither")
