#! /Users/tony/anaconda3/bin/python3
'''
Python process argument
'''
import sys

def main_method():
    print("Anaconda Python Platform")
    print(sys.argv)
    print(len(sys.argv))
    if(len(sys.argv) == 1):
        print("Missing arguments for this program ! ")
    else:
        print("Processing the detail logic ")
if __name__ == "__main__":
    main_method()
