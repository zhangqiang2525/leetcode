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


"""
方法二应该注意的点在于当nums中出现两个相同的数相加等于target时如何取下标
判断i是否等于nums.index(目标元素)
"""


def two_sum1(nums, target):
    for i in range(len(nums)):
        a = target - nums[i]
        if a in nums:
            b = nums.index(a)
            if b == i:
                continue
            else:
                return i, b


"""
tips:
在使用字典的过程中应避免出现相同的key，
如果出现相同的key，第二个key对应的value会覆盖第一个key的value
因此elif nums[i] not in d就是用来避免上述的值
"""


def two_sum2(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:  # 如果目标值 - nums中的值在字典d中，则返回对应的key和数组下标
            return d[target - nums[i]], i
        elif nums[i] not in d:  # 如果nums中有两个相同的值则不会添加到字典中
            d[nums[i]] = i


print(two_sum2([2, 7, 7, 15], 22))
