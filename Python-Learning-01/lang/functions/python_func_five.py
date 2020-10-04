#!/Users/tony/anaconda3/bin/python3

def make_func(first, last, *ingredient):
    f_first = first
    f_last = last

    all_items = ingredient
    for item in all_items:
        print(item)


if __name__ == '__main__':
    make_func('Tony','Liu','A','B','C','D')