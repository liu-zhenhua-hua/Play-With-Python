#!/Users/tony/anaconda3/bin/python3


import re

"""
define a text variable
"""
search_text = """
My Phone Numbers:
345-789-3289
897-900-5568
808-111-9090
"""

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #regex object return to phoneRegex

