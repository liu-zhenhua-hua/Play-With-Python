'''
Python List Second Program
'''

my_list = ["First","Second","Third","Fourth","Fifth"]

my_list.insert(0,"Previous-Item") #Adding "Previous-Item" in the First position of the List

print(my_list)

my_list[:0] = ["First-Item"]

print(my_list)

del my_list[0] # delete first element of List

my_list[0:1] = [] # same as del my_list[0]

print(my_list)

my_list = []
print("=====================================================================================")

print("Checking the my_list First ")
print(my_list)

my_list.insert(1,"A")
my_list.insert(1,"B")
my_list[len(my_list):] = ["C"]
my_list[len(my_list):] = ["D"]
my_list[len(my_list):] = ["A"]
my_list[len(my_list):] = ["E"]
my_list[len(my_list):] = ["A"]
print(my_list)

my_list.remove("A") # 先查找给定值的第一个实例, 然后将该值从列表中删除


if 'M' in my_list:
    print("The Element in the List")
else:
    print("We can't find out this Element in the List ")
print(my_list)

