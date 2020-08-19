'''
 Python Regular Package;
 Python Regular Expression Examples
'''
import re;

text_to_search='''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

#print(r'\tTab');

#pattern = re.compile(r'abc');
#pattern = re.compile(r'\.') #just search the '.' please use \. escape the dot
#pattern = re.compile(r'coreyms\.com')
pattern = re.compile(r'\d') #Matching all digit in text_to_search

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)

#print(text_to_search[1:4])
#print(text_to_search[142:153])