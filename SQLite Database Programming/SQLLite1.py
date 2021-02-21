import sqlite3
from employee import Employee  #Import another class

# # conn = sqlite3.connect(':memory:') #to create an in memory database
# conn = sqlite3.connect('employee.db') # use file
#
# c = conn.cursor() #create Cursor to execute SQL commands
# #
# # c.execute("""CREATE TABLE employees(
# #              firstname text,
# #              lastname text,
# #              pay integer
# #             )""")
#
# emp_1 = Employee('Jodha','Bai',50000)
# emp_2 = Employee('Jalaluddin','Akbar',70000)
#
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", ())
# # c.execute("INSERT INTO employees VALUES('Vinod', 'Mehra', 80000) ")
# # c.execute("INSERT INTO employees VALUES('Ertugrul', 'Ghazi', 1000000) ")
#
#
#
# c.execute("SELECT * FROM employees")
# print(c.fetchone()) #returns first matching record
# print(c.fetchall()) # returns remaining results in the form of a list
#
# conn.commit() #Commits current transaction
# conn.close()

#---------------------------USING CLASS REFERENCE-----------------------------------------------------------


# conn = sqlite3.connect(':memory:') #to create an in memory database
conn = sqlite3.connect('employee.db') # use file

c = conn.cursor() #create Cursor to execute SQL commands
#
# c.execute("""CREATE TABLE employees(
#              firstname text,
#              lastname text,
#              pay integer
#             )""")

emp_1 = Employee('Jodha','Bai',50000)
emp_2 = Employee('Jalaluddin','Akbar',70000)

# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) # DB API Placeholder Method
# conn.commit()
#
# #DB API Colon Method
# c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first':emp_1.first, 'last':emp_2.last, 'pay': emp_2.pay})
# conn.commit()


c.execute("SELECT * FROM employees WHERE lastname=?", ('Ghazi',))
print(c.fetchall()) # returns remaining results in the form of a list

c.execute("SELECT * FROM employees WHERE lastname=:last", {'last': 'Akbar'})
print(c.fetchall()) # returns remaining results in the form of a list

conn.commit() #Commits current transaction
conn.close()


