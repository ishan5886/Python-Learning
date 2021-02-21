#Decorators - Function that takes function as an argument, performs some functionality and returns another function

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function





# def decorator_function(original_function):
#     def wrapper_function():
#         return original_function()
#     return wrapper_function
#
# @decorator_function  # Same as display = decorator_function(display)
#
# def display():
#     print('Display function ran')
#
#
# display()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function  # Same as display = decorator_function(display)\
def display():
    print('Display function ran')

@decorator_function  # Same as display_args = decorator_function(display_args)\
def display_args(name, age):
    print('Display function ran with arguments ({}, {})'.format(name, age))

display()
display_args('Ishan', 95)