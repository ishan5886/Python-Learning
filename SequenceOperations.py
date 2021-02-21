
# Sequencing-Continuous collection of data types which allow operations to be performed on them like indexing or slicing

# Operations on Sequences - Concatenation, Repetition,Membership Testing, Slicing,Indexing

list1 = ['A', 'B', 'C']
list2 = ['X', 'Y', 'Z']

# Concatenation

"""
print(list1 + ['D', 'E', 'F'] + list2)
print(list1[1])
print(list1*3)
----------------------------------------------------------------------------------------------
"""

# Slicing -Does not print the last value of index

"""
print(list1[0:2])
print(list1[-1])  # Prints Last Element -Prints List items in reverse
-----------------------------------------------------------------------------------------------
"""

# Membership

"""
print('B' in list1)
print('x' in list2)

------------------------------------------------------------------------------------------------
"""


list3 = [x+2 for x in [1, 2, 3, 4]]
print(list3)
