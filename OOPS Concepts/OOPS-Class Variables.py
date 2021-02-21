# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def appraise(self):   #Without using class variable
#         self.pay = int(self.pay * 1.04)
#
#
# emp_1 = Employee('Ishan', 'Dhaliwal', 90000)
# print(emp_1.pay)
# emp_1.appraise()
# print(emp_1.pay)


#------------------------------------------With Class Variable-----------------------------------------------------#
#
# class Employee:
#
#     raise_amount = 2.50
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def appraise(self):
#         self.pay = int(self.pay * Employee.raise_amount)   # Access Class Variable through ClassName
#         self.pay = int(self.pay * self.raise_amount)       # Access Class Variable through Instance(self)
#
#
# emp_1 = Employee('Ishan', 'Dhaliwal', 90000)
# print(emp_1.pay)
# emp_1.appraise()
# print(emp_1.pay)
# #
# print(emp_1.raise_amount) #Access Class variable through Instance(Self)
# print(Employee.raise_amount) #Access Class Variable through classname
#
# # Employee.raise_amount = 3.00 #syntax to change class variable value
# #
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
#
# emp_1.raise_amount = 4.00 #syntax to change instance variable value
#
# print(emp_1.raise_amount)
# print(Employee.raise_amount)



#---------------------------------------------------------------------------------------------------------------------#

#
# class Employee:
#
#     emp_no = 0
#     raise_amount = 2.50
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#
#         Employee.emp_no += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def appraise(self):
#         self.pay = int(self.pay * Employee.raise_amount)   # Access Class Variable through ClassName
#         self.pay = int(self.pay * self.raise_amount)       # Access Class Variable through Instance(self)
#
#
# emp_1 = Employee('Ishan1', 'Dhaliwal1', 90000)
# emp_2 = Employee('Ishan2', 'Dhaliwal2', 10000)
# emp_3 = Employee('Ishan3', 'Dhaliwa3', 20000)
# emp_4 = Employee('Ishan4', 'Dhaliwal4', 30000)
#
# print(Employee.emp_no)