"""

# print("Hello \n World")  # Basic Print Statement
 ---------------------------------------------
"""


# Variable Declaration in Python

"""
A = 20
B = 'edureka'
print(A, B)  # Printing variable values

x, y, z = 20, 30, 40
print(x, y, z)

------------------------------------------------
"""
"""

# Data Types

Immutable - Values cannot be changed - Numbers , Strings, Tuples
Mutable - Values can be changed - List , Dictionaries, Sets

"""

# NUMBERS - int,float, Complex Numbers
""""
x = 10+4j
y = 5 + 6j
z = y-x
print(z)
"""

# STRINGS - Continuous characters of Strings

"""
A = "Helloooooo"
B = "oooooooo"
print(A, B)
course_name = 'ishan'
print("Welcome to %s. Have a good day" %(course_name)) # Placeholder
"""

# TUPLES - A fixed list of items separated by a comma and enclosed in a parenthesis
# #Can contain items of different data types

"""
tuple1 = (1, 2, 3, 'ishan')
print(A)
print(A[0])  # Print specific element by specifying index - Index begins with 0
print(A[1])
print(A[2])
"""


# LISTS - Similar to tuples but can change value - Enclosed in square brackets

""""
list1 = [4, 5, 6, 'sheldon', 'raj', 'leonard', 'howard']
print(list1)
print(list1[3])  # Print specific element by specifying index - Index begins with 0
print(list1[4])
print(list1[5])

list1[2] = 'ishan'  # Change value of list member by specifying index value
print(list1)


list2 = ([2, 3, 4], 99, (6, 7, 8))  # List and Tuples within a List

print(list2[0][2])  # Access element of list within the list
print(list2[2][1])  # Access element of tuple within a list
del(list1[1]) # Delete an element of a list
print(list1.pop(3)) # Displays element at the index mentioned and then removes it from the list

list3 = [x+2 for x in [1, 2, 3, 4]]  # List Comprehension
print(list3) 
"""

# DICTIONARIES - Key value pairs separated by a colon - Enclosed in curly braces
# Better than lists because more readable
# Key has to be String, Value can be of any Data Type

"""
dict1 = {'Age': 24, 'Name': 'Ishan'}
print(dict1['Age'])
"""

# SETS - Unordered collection of items - Enclosed in curly braces - Each element should be unique

"""
set1 = {1, 1, 1, 1}
print(set1)
"""











