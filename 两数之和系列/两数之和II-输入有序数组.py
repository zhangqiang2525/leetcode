"""
双指针法:
双指针法听起来很高大尚，用大白话来讲就是分别从列表的第一个元素（或下标为0的元素）和最后一个元素(len(nums) - 1)开始找起
在这个方法中对我来说刚开始比较难理解的地方就是numbers[i] + numbers[j] > target，为什么两数相加>target从列表尾部找起的j就要减1，
而答案在题目描述中“给定一个已按照升序排列 的有序数组”此处，请注意“按照升序排列”，当numbers[i] + numbers[j] > target时，必然有j>i,
当j>i时必然j-1喽！
例：
nums = [1,2,3,4,5]
target = 5
1 + 5 > 6
j > i
tips:
在对列表使用双指针时一定要对列表排序
"""


class Solution(object):
    def twoSum(self, numbers, target):
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i + 1, j + 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


class Solution1(object):
    def binary_search(self, num, tar, left, right, if_find_left):
        """
        通过二分法查找目标值-nums[r/l]是否在nus中
        :param num: 数组
        :param tar: sum_>target:target - nums[r];sum_<target:target - nums[l]
        :param left: sum_>target : l ;sum_<target : l+1
        :param right: sum_>target : r - 1 ;sum_<target : r
        :param if_find_left: True / False
        :return: 
        """
        while left <= right:
            mid = (left + right) // 2
            if num[mid] < tar:
                left = mid + 1
            elif num[mid] > tar:
                right = mid - 1
            else:
                return mid
        return left if if_find_left else right

    def twoSum(self, numbers, target):
        """
        双指针法
        :param numbers: 数组
        :param target: 目标值
        :return:
        """
        l, r = 0, len(numbers) - 1  # 取数组首尾元素下标
        while l < r:
            sum_ = numbers[l] + numbers[r]  # 取下标为l,r元素的和
            if sum_ < target:  # 与目标值作比较
                l = self.binary_search(numbers, target - numbers[r], left=l, right=r, if_find_left=True)
            elif sum_ > target:
                r = self.binary_search(numbers, target - numbers[l], left=l, right=r, if_find_left=False)
            else:
                return [l + 1, r + 1]



s = Solution1()
print(s.twoSum([1, 2, 5, 5, 7], 10))
