#! /Users/tony/anaconda3/bin/python3
'''
Python read a file program
'''
import sys #import the sys module for process arguments which user passed.
def read_file(file_name,mode):
    with open(file_name,mode) as file_obj:
        line = file_obj.readline()
        print(line)

def main_proc():
    arguments = sys.argv
    if(arguments.__len__() < 3):
        # print(arguments)
        print("-- Usage ./read_file.py file_name mode (mode->r read,w write...) ")
    else:
        read_file(arguments[1],arguments[2])

if __name__ == "__main__":
    main_proc()