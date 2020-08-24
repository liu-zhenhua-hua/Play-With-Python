'''
 Python Regular Package;
 Python Regular Expression Examples
 Python Regular Exp Programs, and Practices
'''
import re;

text_to_search='''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

lalida_mail@gmail.com

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

cat
mat
pat
bat

'''

sentence = 'Start a sentence and then bring it to an end'

email_address = ''' atomic_tony@169.com '''

my_email_address = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


#print(r'\tTab');

#pattern = re.compile(r'abc');
#pattern = re.compile(r'\.') #just search the '.' please use \. escape the dot
#pattern = re.compile(r'coreyms\.com')
#pattern = re.compile(r'\d') #Matching all digit in text_to_search
#pattern = re.compile(r'\w') #Word Character (a-z, A-Z,0-9,_)
#pattern = re.compile(r'\W') #Not a Word Character.
#pattern = re.compile(r'\bHa') #Word Boundary
#pattern = re.compile(r'\BHa') #Not a Word Boundary
#pattern = re.compile(r'^Start') #Begining of a String

#pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #fetching Phone Number in text_to_search

#pattern = re.compile(r'[a-z]') #Character Range from a-z lower case, or [a-zA-Z] lower case and Capital case
#pattern = re.compile(r'[^a-zA-Z]') #Characters Not In Brackets
#pattern = re.compile(r'[^b]at') #Three Characters we want to search, not start with 'b'
#pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') #Try to practice this Regular Expression

pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
pattern = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(com|edu)')
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')


pattern = re.compile(r'[a-zA-Z0-9_.+-]+@')
matches = pattern.finditer(my_email_address) #text_to_search
for match in matches:
    print(match)

#print(text_to_search[1:4])
#print(text_to_search[142:153])
