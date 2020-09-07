'''
Python read a file program
'''

def read_file(file_name,mode):
    with open(file_name,mode) as file_obj:
        line = file_obj.readline()
        print(line)

if __name__ == "__main__":
    read_file()