# def hello_func():    #Declare function using def keyword
#     print("Hello Function")
#
# hello_func()   #How to call a function

#----------------------------- Passing Arguments to Function----------------------------------------------------

# def hello_func(greeting):
#     return '{} Function '.format(greeting)
#
# print(hello_func('Hi'))




# def hello_func(greeting, name):
#     return '{}, {} Function '.format(greeting, name)
#
# print(hello_func('Hi', 'Ishan'))


# -------------- *args and **kwargs ----------------------------------------------------------#

#Accept arbitrary number of positional arguments

def student_info(*args, **kwargs):
    print(args)  #Tuple with positional arguments
    print(kwargs)  #Dictionary with keyword arguments

student_info('Maths', 'Art', name='Ishan1', age=33)


