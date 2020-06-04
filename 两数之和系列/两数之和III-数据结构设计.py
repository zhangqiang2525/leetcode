"""
这道题在解题的过程中不熟悉的点：
1.python的初始化类
2.两数之和的多种解法
"""


# 方法一
class TwoSum(object):

    def __init__(self):
        self.nums = []  # 初始化一个列表

    def add(self, number):
        self.nums.append(number)    # 将number添加到列表中

    def find(self, value):
        self.nums.sort()    # 排序
        l, r = 0, len(self.nums) - 1    # 双指针方法求列表中两元素之和是否=target
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] > value:
                r -= 1
            else:
                l += 1
        return False


# 方法二
class TwoSum1(object):
    def __init__(self):
        self.d = {}     # 初始化字典

    def add(self, number):
        if number in self.d:
            self.d[number] += 1     # 如果number存在字典中，则令value+1，应对两个相对元素相加=target的情况（例如3+3=6）
        else:
            self.d[number] = 1      # 如果不存在，则令value=1

    def find(self, value):
        for number in self.d.keys():    # 依次遍历字典的key
            a = value - number
            if a != number:    # 如果目标值-numer != number 且存在字典中返回True
                if value - number in self.d:
                    return True
            elif self.d[number] > 1:    # 如果出现两个相同的值，则后加入的元素的value > 1
                return True

        return False
