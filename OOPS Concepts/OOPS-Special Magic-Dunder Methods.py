class Employee:

    emp_no = 0
    raise_amt = 2.50

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.emp_no += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def appraise(self):
        # self.pay = int(self.pay * Employee.raise_amt)   # Access Class Variable through ClassName
        self.pay = int(self.pay * self.raise_amt)       # Access Class Variable through Instance(self)

#
# emp_1 = Employee('Ishan1', 'Dhaliwal1', 90000)
# emp_2 = Employee('Ishan2', 'Dhaliwal2', 10000)
# emp_3 = Employee('Ishan3', 'Dhaliwa3', 20000)
# emp_4 = Employee('Ishan4', 'Dhaliwal4', 30000)

class Developer(Employee):                    #ClassName(ParentClassName)
    raise_amt = 1.10   #Modify raise_amt value for Developer class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)   #Parent class handles arguments mentioned inside init
        self.prog_lang = prog_lang

    def __repr__(self):
        return "Employee('{}', '{}', '{}', {})".format(self.first, self.last, self.pay, self.prog_lang)

    def __str__(self):
        return '{}'.format(self.fullname())


dev_1 = Developer('Ishan1', 'Dhaliwal1', 90000, 'Python')
dev_2 = Developer('Ishan2', 'Dhaliwal2', 10000, 'Java')
dev_3 = Developer('Ishan3', 'Dhaliwa3', 20000, 'C++')
dev_4 = Developer('Ishan4', 'Dhaliwal4', 30000, 'R')

# Employee.set_raise_amt(3.25)
#
# #print(help(Developer))  #Method Resolution Order, Methods Inherited etc
# print(dev_1.prog_lang)
# # dev_1.appraise()
# print(dev_2.prog_lang)
#
# print(isinstance(dev_1, Developer))  #Print if instance belongs to that class
# print((issubclass(Developer,Employee)))  #Print if class is subclass of another class


print(repr(dev_1))
print(str(dev_1))

