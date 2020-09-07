#! /User/tony/anaconda3/bin/python3
"""
Python File redirect
"""
import sys

f = open("outfile.txt",'w')
sys.stdout = f
sys.stdout.writelines(["A First Line .\n","B Second Line.\n"])
print("C Third Line.\n")


sys.stdout = sys.__stdout__
f.close()


f = open("secondOutfile.txt",'w')
print("A First Line \n","B Second Line. \n",file=f)

f.close()