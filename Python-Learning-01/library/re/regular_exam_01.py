#!/Users/tony/anaconda3/bin/python3

import re

"""
Python Regular Expression Example-01
"""

original_text = """
899-897-9098
457-456-1256
887=MLK=9807
"""

pattern = re.compile(r'\d{3}=\w+=\d{4}') # 匹配887=MLK=9807
matches = pattern.finditer(original_text)

for items in matches:
    print(items)


print("=" * 90)

original_numbers = """
899-897-9098
457-456-1256
887=MLK=9807
670#BNM#7856
809^BHU^8900
"""

"""
从 original_numbers 中匹配下面这些值
887=MLK=9807
670#BNM#7856
809^BHU^8900
"""
pattern = re.compile(r'\d{3}(=|#|\^)\w+(=|#|\^)\d{4}')
matches = pattern.finditer(original_numbers)
for items in matches:
    print(items)


print("=" * 90)


original_name_list = """
Ms. Schafer
Mr. Bourne
Ms. Taras
Mrs. T 
"""

