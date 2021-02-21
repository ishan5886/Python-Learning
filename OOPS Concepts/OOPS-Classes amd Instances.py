# class Employee:
#     pass
#
# # emp_1 = Employee() #Instance of class
# # emp_2 = Employee()
# #
# # emp_1.first = 'Ishan'
# # emp_1.last = 'Dhaliwal'
# #
# # emp_2.first = 'XXXXX'
# # emp_2.last = 'OOOOO'
# #
# # print(emp_1.first)
# # print(emp_2.last)

#------------------------------------------------------Through Self(init menthod)----------------------------------#
#
# class Employee:
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#
#
# emp_1 = Employee('Ishan', 'Dhaliwal')
# print(emp_1.first)

#------------------------------------------------------Methods in Class-------------------------------------------#

''' Each METHOD in a CLASS automatically takes the instance(self) as first argument

Self is automatic instance of a class and is passed down to all the instance we create for the class

If a method in a class is declared without self argument then whenever an instance calls that method it will give
argument error

'''

class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ishan', 'Dhaliwal')
print(emp_1.fullname())




