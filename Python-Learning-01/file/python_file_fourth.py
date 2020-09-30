#!/Users/tony/anaconda3/bin/python3


"""
Copy the content of file into another file
"""

print("=" * 30 + "Copy File's Content " + "=" * 30)

with open('my_file.txt','r') as rf:
    with open('new_my_file.txt','w') as wf:
        for lines in rf:
            wf.writelines(lines)


