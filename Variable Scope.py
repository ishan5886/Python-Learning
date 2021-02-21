'''

LEGB - Local , Enclosing, Global, Built-in (Order)

'''


# Local - Variable defined within the function



'''--------------------------------# Enclosing----------------------------------------------'''

# x = 'global x'
#
#
# def outer():
#     x = 'outer x'  # x variable local to outer function
#
#     def inner():
#         x= 'inner x'   # x variable local to inner function
#         print(x)       # print value of x in inner function
#     inner()
#     print(x)          # print value of x in outer function
#
# outer()
#
# print(x)  # print value of global x  variable

#------------------------------------------------------------------------------------------------------


#
# def outer():
#     x = 'outer x'  # x variable local to outer function
#
#     def inner():
#
#         print(x)       # print value of x from outer function since no x variable defined in inner function.
#                        # The next instance of x is present in enclosing outer function
#     inner()
#     print(x)          # print value of x in outer function
#
# outer()


'''----------------------------------------------------------------------------------------------------'''

# Non local


def outer():
    x = 'outer x'  # x variable local to outer function

    def inner():
        nonlocal x     # If we need to change value of x in enclosing outer function from inner function
                       # We can work with local variable of our enclosing function
        x = 'inner x'
        print(x)       # print value of x from outer function since no x variable defined in inner function.
                       # The next instance of x is present in enclosing outer function
    inner()
    print(x)          # print value of x in outer function

outer()

'''--------------------------------------------------------------------------------------------------'''
# Global

# x = 'global x'
#
# def test():
#     y = 'local y'
#     # print(y)  # Print value of local variable y
#     print(x)    # Print value of global variable x since global variable is accessible everywhere
#
# test()
#
# # print(y)  # Will throw error as y is local variable and inaccessible outside the function
# print(x)  # Global variable x will print anywhere

# #---------------------------------------------------------------------------------------------------
#
# x = 'global x'
#
# def test():
#     x = 'local x'
#     # print(y)  # Print value of local variable y
#     print(x)    # Print value of local variable x since order of search is LEGB
#
# test()
# # print(y)  # Will throw error as y is local variable and inaccessible outside the function
# print(x)  # Global variable x will print anywhere

#---------------------------------------------------------------------------------------------------

x = 'global x'

# def test():
#     global x   # Explicitly telling that the x variable is global
#     x = 'local x' #Setting value of global x variable
#     # print(y)  # Print value of local variable y
#     print(x)    # Print value of global variable x set locally to 'local x'
#
# test()
# # print(y)  # Will throw error as y is local variable and inaccessible outside the function
# print(x)  # Since x is global inside function so will print the updated value of global variable x i.e. 'local x'

#---------------------------------------------------------------------------------------------------------------

# def test(z):   # Parameter z is a local variable inside function... not accessible outside function
#
#     x = 'local x' #Setting value of global x variable
#     # print(y)  # Print value of local variable y
#     print(z)    # Print value of local variable z set locally to 'local x'
#
# test('local z')
# # print(y)  # Will throw error as y is local variable and inaccessible outside the function
# print(z) # z is local variable and not accessible outside function

'''------------------------------------------------------------------------------------------------'''
# Built In

# import builtins
# print(dir(builtins))
# m = min([5,2,6,14,9,11])  # min is built in functions
# print(m)
#
# def min():
#     pass
#
#
#
# def test(z):
#
#     x = 'local x'
#     # print(y)
#     print(z)