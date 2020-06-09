# 修改字符串的大小写
# name = 'zhangqiang'
# print(name.title())     # 首字符大写
# print(name.upper())     # 全部大写
# print(name.lower())     # 全部小写


# 字符串的拼接
# first_name = 'zhang'
# last_name = 'qiang'
# l = first_name + ' ' + last_name
# print(l)


# name = 'Eric'
# l1 = 'Hello ' + name + '，would you ....?'
# l2 = 'Hello ' + name.upper() + '，would you ....?'   # 字母大写
# l3 = 'Hello ' + name.lower() + '，would you ....?'   # 字母小写
# print(l1)
# print(l2)
# print(l3)


name = '\tzhangsan\t\n'
print(name.lstrip())    # 去除字符左边的空格
print(name.rstrip())    # 去除字符右边的空格
print(name.strip())     # 去除全部空格
