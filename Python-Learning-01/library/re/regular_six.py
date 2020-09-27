#!/Users/tony/anaconda3/bin/python3

import re

our_phone_numbers = """
890-145-8946 
326-226-6433

"""

pattern = re.compile(r'\d\d\d')
matches = pattern.finditer(our_phone_numbers)

for items in matches:
    print(items)
