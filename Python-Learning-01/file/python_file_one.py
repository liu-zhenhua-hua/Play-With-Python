#!/Users/tony/anaconda3/bin/python3

"""
Python File Object
"""

f = open('my_file.txt','r') #built-in function open()

print(f.name)
print(f.mode)

f.close() #close the file release the source.
