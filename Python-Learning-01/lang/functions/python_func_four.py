#!/Users/tony/anaconda3/bin/python3

def make_dinner(piece,*ingredient):
    print('Customer want to order ' + str(piece) + ' of dinner !')

    for items in ingredient:
        print("- " + items)

"""
这个函数是个很好的例子
"""
def collect_person_info(first, last, *team_members, **member_info):
    """collect person information """
    all_members = team_members
    for member in all_members:
        print(member)
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in member_info.items():
        profile[key] = value
    print(profile)

if __name__ == '__main__':
    make_dinner(2,'Fried','Peper','Apple','Vegetables')

    collect_person_info('Mark','Zhang','James','William','Ray','Mercy',age=12,location='Dalian')