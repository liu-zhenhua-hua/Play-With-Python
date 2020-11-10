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


fourthMessage = 'My name is {}. Next Year I will be {}'.format(name,age+1)
print(fourthMessage)

"""
upper(), lower(), isupper(), islower() Methods
"""

"""
upper(), lower() string methods return a new string, 
"""

spamMessage = 'Hello,World'
spamMessage = spamMessage.upper()
print(spamMessage)