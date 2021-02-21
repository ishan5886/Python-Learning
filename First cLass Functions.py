# def square(x):
#     return x*x
#
# f = square   # f is now equal to square function
#
# print(f(5))  #F can now take argument of square

#--------------------------------USE ONE FUNCTION AS ARGUMENT IN ANOTHER FUNCTION------------------------------------#

# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
#
# squares = my_map(square, [1, 2, 3, 4, 5])
# print(squares)


#--------------------------------RETURN ONE FUNCTION IN ANOTHER FUNCTION------------------------------------#
#
def logger(msg):
    def log_message():
        print('Log : ', msg)
    return log_message

log_hi = logger('Hi!')
log_hi()


