#!/Users/tony/anaconda3/bin/python3

"""
define a Python function, pass argument based on the position type
"""
def describe_pet(animal_type, animal_name):
    """describe the pet"""
    print("I have a " + animal_type + ". ")
    print("My " + animal_type + "'s name is " + animal_name.title() + ". ")



"""
define a function which has a default value for parameter.
形参列表中必须先列出没有默认值的形参, 再列出有默认值的形参
"""
def describe_person(firstname, lastname, gender='Male'):
    """The functill will describe the person """
    print('The FirstName is ' + firstname + ", SecondName is " + lastname + " Gender is : " + gender)




if __name__ == '__main__':

    """
        position parameter passing style
    """
    describe_pet('hamster','harry')

    """
        Key-Value parameter passing style
    """
    describe_pet(animal_type='hamster',animal_name='harry')

    """
        the function has default value 
    """
    describe_person('Liu', 'Mark')
    describe_person('Zhang','Lucy','Female')