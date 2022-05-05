from typing import List


from typing import List


def findZero(nums : List[int]):
    result = []
    for i in nums:
        for j in nums[i+1:]:
            for k in nums[j+1:]:
                if i + j + k == 0:                
                    result.add(set([1,2,3]))

    
    return result

if __name__ == "__main__":

    """
    14清水
    1瓶毒药
    4只小白鼠
    一天时间
    毒药生效时间1天
    1111
    8 + 4 + 2 + 1
    
    """
    # s1 = set()
    # s1.add(1)
    # s1.add(2)
    # s1.add(3)
    # s2 = set()
    # s2.add(2)
    # s2.add(1)
    # s2.add(3)
    # print(s1 == s2)
    # print(set([1,2,3]))
    print(findZero([-1, 0, 1, 2, -1, -4]))