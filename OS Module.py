import os
from datetime import datetime
# print(dir(os))  #Provides all attributes and methods accessible in the os module

# print(os.getcwd()) #Current work directroy info
os.chdir('D:\Python Programs')  #navigates to the directory specified in the ''
# print(os.getcwd()) # prints new cwd

#print(os.listdir()) #prints all files and folders present in the cwd

#os.mkdir('OSDemo')  #Create new folder OSDemo in cwd upto one level

#os.makedirs('IshanOS/OSDemo') # create all folders in  case we need to make deep level directory

#mkdir can create directory only upto 1 level whereas we can create multiple level directory using makedirs

# os.rmdir('OSDemo') #Remove dir/folder OSDemo
# os.removedirs('IshanOS/OSDemo') #Remove multi level directories

# print(dir(os))

# os.rename('originalfilename', 'newfilename')  #Rename folder

#os.stat(filename)  #stats for filename
#
# for dirpath, dirnames, filenames in os.walk(os.getcwd()):  #Walking the directory
#     print('Current Path: ', dirpath)
#     print('Directory Names: ', dirnames)
#     print('File Names: ', filenames)

# print(os.environ().get('HOME'))

fp = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(fp)



