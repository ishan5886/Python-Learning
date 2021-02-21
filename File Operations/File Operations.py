#File Objects

#----------------------------------------------READING FILES----------------------------------------------------------#
# with open('FileOperations.txt', 'r') as f:    #Context managers - Dont need to close the file
     # f_contents =  f.read()
     # print(f_contents)

     # f_contents = f.readlines()  #Prints all the lines of a file as different elements sperated by a newline(\n)
                                   # character
     # print(f_contents)
#----------------------------------------------------------------------------------------------------------------------
     # f_contents = f.readline()  # Prints the first line of a file and moves to a new line..Newline comman(/n) not
                                  # printed here but adds a extra newline
     # print(f_contents)          # If multiple lines need to be printed then multiple readline commands need to be
                                  # written
# --------------------------------------------------------------------------------------------------------------------
#
#      f_contents = f.readline()
#
#      print(f_contents, end='') # Does not insert a newline character after every line
# --------------------------------------------------------------------------------------------------------------------

     # f_contents = f.read(12)  #prints first 12 characters from the file
     # print(f_contents)
# --------------------------------------------------------------------------------------------------------------


#Outside the scope of context manager file is automatically closed and no operations can be performed on it

# f = open('FileOperations.txt', 'r') # Opens file  r- Read w- Write a- Append
# print(f.name) # Prints name of the file opened
# print(f.mode)  # Mode in which file is opened
# f.close() # Need to close open file

# ----------------------------------------------WRITING FILES---------------------------------------------------------#

# with open('FileWriteOps.txt', 'w') as f:
#     f.write('Test')  # Write text to file
#     f.write('Test2')

#-------------------------------------------------------------------------------------------------------------------#
#
# with open('FileReadWriteOps.txt', 'r') as rf:
#     with open('FileReadWriteOps2.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)   #Writes each line in File1 to File2


# with open('IMG_3217.jpg', 'rb') as rf:
#     with open('IshanCopy.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)  #Make a copy(Image2) of Image1....But must be in the same directory
#

with open('FileReadWriteOps.txt', 'r') as rf:
    with open('FileReadWriteOps3.txt', 'w') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) >0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
