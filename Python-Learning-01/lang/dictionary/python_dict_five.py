#!/Users/tony/anaconda3/bin/python3

"""
pprint module, "pretty print"
This is helpful when you want a cleaner display of the items in a dictionary
"""
import pprint

message = 'It was a bright cold day in April, and the clocks were striking \
thirteen.'

count = {}
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1

pprint.pprint(count) #using pprint() method to  display items in Dictionary

