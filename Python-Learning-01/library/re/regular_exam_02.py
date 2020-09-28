#!/Users/tony/anaconda3/bin/python3

import re

"""
Python Regular Expression Example-02
"""

original_message = """
chrome://tnn.google.com
chrome://coreyms.com
chrome://tnn.facebook.com
chrome://tnn.golambda.net
chrome://keras.org

chromes://apache.org
chromes://kafka.org
chromes://tnn.ibm.com
"""

"""
下面输出的结果是
除了tnn开头的字符串儿, 都被提取出来
"""
pattern = re.compile(r'chromes?://[^(tnn\.)](\w+)(\.\w+)')
matches = pattern.finditer(original_message)
for items in matches:
    print(items)


