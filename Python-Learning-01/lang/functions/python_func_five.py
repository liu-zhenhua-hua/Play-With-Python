#!/Users/tony/anaconda3/bin/python3

import operator

def make_func(first, last, *ingredient):
    f_first = first
    f_last = last

    all_items = ingredient
    for item in all_items:
        print(item)

def calculate_value(firstv, secondv):
    return operator.mul(firstv, secondv)

def find_min_value(firstv, secondv):
    return min(firstv, secondv)


if __name__ == '__main__':
    make_func('Tony','Liu','A','B','C','D')

    result = calculate_value(5,8)
    print(result)
    print(max(5,16))
    print(find_min_value(89,120))