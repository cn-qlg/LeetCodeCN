from random import choice


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indexes = dict()

    def insert(self, val: int) -> bool:
        if val in self.indexes:
            return False
        self.values.append(val)
        self.indexes[val] = len(self.values) -1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indexes:
            return False
        index = self.indexes[val]
        self.values[index] = self.values[-1]
        self.indexes[self.values[index]] = index
        del self.values[-1]
        del self.indexes[val]
        return True
        

    def getRandom(self) -> int:
        return choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
结题思路：
1. 这题本身不难，但是会有一些坑。首先随机读取，虽然很多语言内实现的map（或者dict）结构本身是无序的，但是无序和随机读取是不同的。其次，就是考察随机函数使用。
2. O(1)时间插入，删除可以通过hash表（或者字典来解决），但是hash表无法做到随机读取，这里可以借助一个数组来解决。使用数组来存储所有的元素，字典中存储所有元素以及对应的下标。
3. 插入的时候，直接追加到数组中即可，并且将该元素下标记录到字典中。
4. 删除的时候，可以将数组最后一个元素复制到被删除的元素位置，同时更新字典中的数组下标。
5. 随机的时候，通过random.choice来实现。
但是这里有一个问题，不同语言底层实现是不同的：
1. 很多语言的数组在进行添加的时候，如果元素个数超过了底层容量是会发生扩容的，这个时候他的时间复杂度就不是O（1）了。比如Go中的切片
2. Go中的map虽然是无序的，似乎可以通过遍历的时候返回第一个元素来解决随机问题。但是实际执行中，不够随机，而题目中要求每个元素返回的概率相同。
"""