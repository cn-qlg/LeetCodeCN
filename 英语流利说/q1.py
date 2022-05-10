"""有序数组，统计任意两个值等于目标值的个数
"""
def addToN(nums, des):
    i = 0
    j = len(nums) - 1
    res = 0
    while i < j:
        if nums[i] + nums[j] == des:
            res += 1
            m, n = 1, 1
            i += 1
            while i < j and nums[i] == nums[i-1]:
                m += 1
                i += 1
            j -= 1
            while i < j and nums[j] == nums[j+1]:
                n += 1
                j -= 1
            res += m * n - 1
        elif nums[i] + nums[j] < des:
            i += 1
        else:
            j -= 1
    return res


print(addToN([1, 1, 2, 3, 4, 5, 6, 7, 7], 8))
