#!/Users/tony/anaconda3/bin/python3

g_number_one = 1
g_number_two = 1


def calculate_value(first_value):
    l_first_value = first_value
    globals()['g_number_one'] = 20
    l_first_value = l_first_value + g_number_one
    return l_first_value

result = calculate_value(10)
print('The Result is ' + str(result))
print('The global value One : ' + str(g_number_one))
print('The global value Two : ' + str(g_number_two))