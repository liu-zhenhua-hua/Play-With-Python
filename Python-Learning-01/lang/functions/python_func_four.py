#!/Users/tony/anaconda3/bin/python3

def make_dinner(piece,*ingredient):
    print('Customer want to order ' + str(piece) + ' of dinner !')

    for items in ingredient:
        print("- " + items)


def collect_person_info(first, last, *team_members, **member_info):
    """collect person information """


if __name__ == '__main__':
    make_dinner(2,'Fried','Peper','Apple','Vegetables')