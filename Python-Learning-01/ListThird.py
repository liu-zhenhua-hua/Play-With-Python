'''
Python ListThird Program
'''

my_list = [1,2,8,9,34,20,28]
print(my_list)
my_list.sort()
print(my_list)


# my_list = [45,90,190,28,"B","C","A"] # 报错, 元素之间是可比较的
# print(my_list)
# my_list.sort()

"""
 list-1 + list-2 拼接两个列表
"""

alist_one = ["A","B","C"]
blist_two = ["D","E","F"]

print(alist_one + blist_two)


"""
使用 * 初始化list
"""

alist_three = [None] * 5 # 生成五个元素为None的列表
print(alist_three)

alist_three[0] = "cmake"

print(alist_three)


alist_four = ["String"] * 7
print(alist_four)

alist_five = [4,5,9,10] * 3
print(alist_five)


alist_six = ['A','C',89,80,100,"GNU","MMK"]
# alist_six.index("PSCS") #不存的元素会报错, 找到元素, 返回元素所在的位置（索引）
print(alist_six.index("GNU"))