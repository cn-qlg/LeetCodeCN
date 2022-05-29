class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        targetDic = dict()
        for c in target:
            if c in targetDic:
                targetDic[c] += 1
            else:
                targetDic[c] = 1
        sDict = dict()
        for c in s:
            if c in sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        
        minRep = len(s)
        # print(targetDic, sDict)
        for k, v in targetDic.items():
            if k not in sDict:
                return 0
            rep = sDict[k] // v
            if rep < minRep:
                minRep = rep
        return minRep

if __name__ == "__main__":
    print(Solution().rearrangeCharacters("ilovecodingonleetcode","code"))
    print(Solution().rearrangeCharacters("abcba","abc"))
    print(Solution().rearrangeCharacters("abbaccaddaeea","aaaaa"))
