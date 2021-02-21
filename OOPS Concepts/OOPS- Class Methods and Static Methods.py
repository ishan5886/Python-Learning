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
        self.pay = int(self.pay * Employee.raise_amt)   # Access Class Variable through ClassName
        self.pay = int(self.pay * self.raise_amt)       # Access Class Variable through Instance(self)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True



emp_1 = Employee('Ishan1', 'Dhaliwal1', 90000)
emp_2 = Employee('Ishan2', 'Dhaliwal2', 10000)
emp_3 = Employee('Ishan3', 'Dhaliwa3', 20000)
emp_4 = Employee('Ishan4', 'Dhaliwal4', 30000)

# Employee.set_raise_amt(3.25)
#
# print(emp_1.raise_amt)


#--------------------------------STATIC METHODS----------------------------------------------------------#

# Dont pass cls or self as first argument automatically


import datetime
my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))





