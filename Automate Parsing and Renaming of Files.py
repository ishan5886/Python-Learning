import os

os.chdir('D:\Python Programs\Ishan\Test Data for Parsing and Renaming Files')
# print(os.getcwd())

for f in os.listdir():
    #     print(f)
    #    print(os.path.splitext(f))  #Gives tuple splitting file text
    file_name, file_ext = os.path.splitext(f)   #Split file into root name and extension
    # print(file_name)  # prints file name
    # print(file_name.split('-')) # Splits filename into three variables preceeding dash

    f_upper, f_lower, f_num = file_name.split('-') #Splits strings into three variables which were seperated by dash
    # # print(f_upper)
    # # print(f_lower)
    # # print(f_num)

    f_upper = f_upper.strip()  #Stripping unnecessary spaces
    f_lower = f_lower.strip()
    #f_num = f_num.strip()[1:]  #Will strip first character and read characters after that
    f_num = f_num.strip()[1:].zfill(2) #Will make the f_num string 2 digit wide...Depending on the parameter number in zfill
    # print('{}-{}-{}{}'.format(f_num,f_upper,f_lower,file_ext))
    new_name = '{}-{}-{}{}'.format(f_num,f_upper,f_lower,file_ext)
    os.rename(f, new_name)