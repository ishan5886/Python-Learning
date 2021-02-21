first_name = 'Ishan'
last_name = 'Dhaliwal'

# sentence = f'My Name is {first_name} {last_name}'  #Can add variable name within placeholder
# print(sentence)

# sentence = f'My Name is {first_name.upper()} {last_name.lower()}'  #Can add function name within placeholder
# print(sentence)


#---------------------------------FString with Dictionaries----------------------------------------------###

# person = {'name': 'Ishan', 'age': 33}
#
# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)

#------------------------------------------Calculation within F-String---------------------------------------#
# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)

#------------------------------------------F-String Looping---------------------------------------#

# for n in range(1, 11):
#     sentence = f'The value is {n:03}' # Value of n Padded to 3 digits like 00n
#     print(sentence)

#------------------------------------------F-String Formatting with DateTime---------------------------------------#

from datetime import datetime

birthday = datetime(1990, 1, 1)

sentence = f'Jenn has a birthday on {birthday:%w, %B, %Y, %A}'
print(sentence)







