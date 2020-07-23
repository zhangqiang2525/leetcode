class Solution(object):
    def heightChecker(self, num_list):
        sort_list = sorted(num_list)
        print(sort_list)
        flag = 0
        for i in range(0, len(num_list)):
            if sort_list[i] != num_list[i]:
                flag += 1
        return flag


s = Solution()
print(s.heightChecker([1, 3, 7, 1, 1, 2, 6]))
