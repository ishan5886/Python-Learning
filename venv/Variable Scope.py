'''
LEGB(Local, Enclosing,Global,Built-in)
'''

#*********************************----------LOCAL AND GLOBAL VARIABLE------*****************************#

x = 'global x'

'''
def test():
    y = 'local y'
    print(y)   #Prints 'local y' as y is local variable

test()

def test():
    print(x)   #Prints 'global x' as x is global variable

test()

'''

'''
def test():
    global x  # Access global variable x inside function
    x = 'local x'
    print(x)   # Prints 'local y' as y is local variable

test()  # Print value of local x variable i.e. 'local x'
print(x) # Print value of local variable x i.e. 'local x' since new value of x is set inside the function
'''


'''
def test(z):

    print(z)   # Prints 'local z' as z is local variable

test('local z')  # Print value of local x variable i.e. 'local x'
#print(z) # Print value of local variable z i.e. 'local z' since value of z is set inside the function
'''


#***************************---------------------Built In Variables Scope---------------**************************#

''' 
m = min([5,3,4,14,2,8])
print(m)
'''

#***************************---------------------Enclosed Variables Scope---------------**************************#
'''
x= 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)  # Prints value of local variable x inside inner

    inner()
    print(x) # Prints value of local variable x inside outer

outer()
'''
'''
x= 'global x'

def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)  # Prints value of local variable x inside enclosing function outer

    inner()
    print(x) # Prints value of local variable x inside outer

outer()

'''
'''
x= 'global x'

def outer():
    # x = 'outer x'

    def inner():
      #  x = 'inner x'
        print(x)  # Prints value of global variable x since x not present in method or any any enclosing method

    inner()
    print(x) # Prints value of global variable x

outer()
print(x)
'''



def outer():
    x = 'outer x'

    def inner():
        nonlocal x   #Searches for next  x variable not local to function(here in outer function)
        x = 'inner x' #Modifies value of nonlocal variable x inside outer function
        print(x)  # Prints value of local variable x inside inner

    inner()
    print(x) # Prints value of local variable x inside outer as modified value 'inner x' since value modified in inner function
outer()
print(x)









