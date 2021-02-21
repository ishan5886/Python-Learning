nums = [1,2,3,4,5,6,7,8,9,10]

# Example 1  - Normal for loop -  n for each n in nums

# # my_list = []
# # for n in nums:
# #     my_list.append(n)
# # print(my_list)
#
#
# my_list = [n for n in nums]  # Comprehension
# print(my_list)


'''------------------------------------------------------------------------------------------'''

# Example 2  - Normal for loop - n*n for each n in nums

# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

#
# my_list = [n*n for n in nums]  # Comprehension  [ReturnValue for EachItem in TestData]
# print(my_list)


'''------------------------------------------------------------------------------------------'''

# Example 3  - Normal for loop - n for each n in nums if n is even

# my_list = []
# for n in nums:
#       if n%2 ==0:
#           my_list.append(n)
# print(my_list)


# my_list = [n for n in nums if n%2 == 0]  # Comprehension  ([ReturnValue] for [EachItem] in [TestData] if [Condition])
# print(my_list)


'''------------------------------------------------------------------------------------------'''

# Example 4  -  Nested For Loop - A (letter,num) pair for each letter in 'abcd' and each number in '0123'
#
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter,num))
# print(my_list)


# Comprehension  ([ReturnValue] for [EachItem] in [TestData] if [Condition])
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
#
# # [Return Value] variable names should be exactly same with those used in [Each Item] variables
# print(my_list)


'''------------------------------------------------------------------------------------------'''

# Example 5  -  Dictionary Comprehensions - I want a dict{'name': 'hero'} for each name,hero in zip(names,hero)

names = ['B', 'C', 'D', 'A', 'T']
hero = ['W', 'X', 'Y', 'Z', 'F' ]

# print(zip(names,hero))

# my_dict = {}
# for name, heros in zip(names, hero):
#     my_dict[name] = heros
#
# print(my_dict)

# Comprehension  ([ReturnValue] for [EachItem] in [TestData] if [Condition])
my_dict = {name: heros for name,heros in zip(names,hero)}
# [Return Value] variable names should be exactly same with those used in [Each Item] variables

print(my_dict)