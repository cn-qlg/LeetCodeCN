"""
解题思路：
一开始的思路就是map嵌套map，但是看了一下题目单词最长2000，所以，最坏可能是2000个map嵌套，觉得不太可能。看解题思路，结果还是同样的。那就开始写吧。
第一个版本没考虑结束符，准备直接把所有数据写到map中，没有类的嵌套，所以如果出现这种情况：
class Trie:

    def __init__(self):
        self.data = {}
    插入的时候就依次遍历，当前key不存在，就插入
    所以，apple插入之后会变成这样{"a}    

已有：apple，需要查找：app，

"""
class Trie:

    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word: str) -> None:
        current = self
        for c in word:
            if c not in current.children:
                current.children[c]= Trie()
            current = current.children[c]
        current.end = True        

    def search(self, word: str) -> bool:
        current = self
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.end

    def startsWith(self, prefix: str) -> bool:
        current = self
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True
    
    def __str__(self) -> str:
        return str(self.children)
    
    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    print(t.startsWith("app"))
    print(t.startsWith("ac"))
    print(t.search("app"))
    print(t.search("apple"))
    print(t.search("applea"))

