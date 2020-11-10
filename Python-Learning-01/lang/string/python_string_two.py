#!/Users/tony/anaconda3/bin/python3


name = 'AI'
age = 4000

message='Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'

print(message)

#==================================================================================

secondMessage = 'My name is %s. I am %s years old. '%(name,age)

print(secondMessage)

#==================================================================================

thirdMessage = f'My name is {name}. Next year I will be {age+1}.'

print(thirdMessage)
