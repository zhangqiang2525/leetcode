# 两数之和的三种解法
# 方式1

"""
i,j是用来寻找相加等于target的两个数,
j从i+1开始是为了防止如果nums中出现两个相同的数（[3,3,6]）不会返回错误的下标
注：nums = [3,3,6],target=6 ,如果j从0开始则返回[0，0]
下标越界问题：
刚开始接触到这道题时，认为i只需要到len(nums) - 1就可以，因为如果i等len(nums)时j就会报错
但是后来发现for j in range(4,3)并不会执行，而不会报错，希望大家可以注意这个点
"""
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return i, j


def two_sum1(nums, target):
    pass