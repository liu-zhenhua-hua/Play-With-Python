#!/Users/tony/anaconda3/bin/python3

import re

"""
匹配email address
"""

my_email_list="""
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

pattern = re.compile(r'[a-zA-z]+@[a-zA-Z]+\.com')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)

print("=" * 90)
"""
下面我们再将其余的email地址取出
"""

pattern = re.compile(r'[a-zA-Z0-9-.]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)

print("=" * 90)

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(my_email_list)
for items in matches:
    print(items)

print("=" * 90)

my_urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(my_urls)
for items in matches:
    print(items)

print("=" * 90 )
"""
我们还可以这样写
"""
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(my_urls)
for items in matches:
    print(items.group(0)) #这里用到了group()方法

print("=" * 90)
"""
urls 如果我们取出domain.com的信息, 可以这样写
"""
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3',my_urls) #这里用了sub方法
print(subbed_urls)