import os

# Reading User Input

"""
#str=input("Enter your input\n")
#print("Received input is\n", str)


name = input("Enter your name\n")
print("Name entered is \n", name)
"""


# -------------------------------------------- FILE OPERATIONS ------------------------------------------------

# file_Object=open(file_name,[access_mode])

# Open File in Write Mode

"""
filenew = open("FileOperations.txt", "w+")
for i in range(1, 5):
    filenew.write("\n File Writing Operations ")
"""

# Open File in Read Mode
""""
filenew = open("FileOps.txt", "r")
for i in range(0, 5):
    print(filenew.read())
"""

# Using os library

"""
os.rename("FileOps.txt", "FileOperations.txt")
"""


"""
filenew = open("FileOperations.txt", "r")
#filenew.close()
print(filenew.mode)  # Specifies mode(read/write) in which file is open
print(filenew.name)

filenew.seek(5)
print(filenew.read())
print(filenew.tell())
"""

