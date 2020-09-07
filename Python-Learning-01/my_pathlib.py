#!/Users/tony/anaconda3/bin/python3
"""
Using Path().write_text(); to save text data(bytes data) into a file
"""
from pathlib import Path
pathlib_textfile = Path("pathlib_file")
pathlib_textfile.write_text("This is text",encoding="UTF-8")


pathlib_textfile2 = Path("pathlib_file2")
pathlib_textfile2.write_text("The Second Path lib File",encoding="UTF-8")



"""
Writing binary data into a file by Path Object
"""
pathlib_binaryfile = Path("my_binary_file")
pathlib_binaryfile.write_bytes(b'Binary File Contents')

print(pathlib_binaryfile.read_bytes())