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
"""


class Solution(object):
    def two_sum(self, numbers, target):
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return i + 1, j + 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


s = Solution()
print(s.two_sum([0, 1, 3, 7, 9, 10, 20, 6, 0, 8, 2, 4], 0))