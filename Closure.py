# def out_func():
#     message = 'Hi'
#
#     def in_func():
#         print(message)
#
#     return in_func
#
#
# my_func = out_func()
# my_func()


#Closure - Inner function that has acces to variables in the local scope in which it was created even if outer function
# was executed

def out_func(msg):
    message = msg

    def in_func():
        print(message)

    return in_func


hi_func = out_func('Hi')
hello_func = out_func('Haloooo')

hi_func()
hello_func()


#Refer Corey Snippets Example