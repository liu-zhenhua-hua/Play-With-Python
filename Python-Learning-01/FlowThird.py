'''
Python, FlowThird
'''

old_list = [1,2,3,4]
new_list = (item * item for item in old_list)

# print(type(new_list)) # now new_list is generator object

for x in new_list:
    print(x)