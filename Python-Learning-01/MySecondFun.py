'''
Python Function with default value
'''


def power(x,y=2):
    r = 1
    while y > 0:
        r = r * x
        y = y-1
    return r

print(power(3))


result = power(y=3,x=2)
print(result)

def find_max_number(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum