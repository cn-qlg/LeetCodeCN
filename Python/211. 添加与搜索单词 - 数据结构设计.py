"""
解题思路：
与208的差别在于处理.，当遇到.的时候，需要遍历当前层来依次判断。
"""

class WordDictionary:

    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word: str) -> None:
        data = self
        for c in word:
            if c not in data.children:
                data.children[c] = WordDictionary()
            data = data.children[c]
        data.end = True

    def search(self, word: str) -> bool:
        data = self
        
        for idx, c in enumerate(word):
            if c == ".":
                for _, v in data.children.items():
                    if v.search(word[idx+1:]):
                        return True
                return False
            if c not in data.children:
                return False
            
            data = data.children[c]
        return data.end
    
    def __str__(self) -> str:
        return str(self.children)
    
    def __repr__(self) -> str:
        return self.__str__()

if __name__ == "__main__":
    wordDictionary =  WordDictionary()
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    print(wordDictionary.search("pad")) # 返回 False
    print(wordDictionary.search("bad")) # 返回 True
    print(wordDictionary.search(".ad")) # 返回 True
    print(wordDictionary.search("b..")) # 返回 True
    print(wordDictionary.search("b.")) # 返回 False
                    
            