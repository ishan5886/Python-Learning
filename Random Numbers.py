import random

# value = random.random()
# print(value)  #prints random value between 0 and 1- 0 and 1 not included


# value = random.uniform(1,100)
# print(value)  #print random value specified in uniform range - integer or float - 1 and 100 not included


# value = random.randint(1,6)
# print(value)  #print random value specified in uniform range - integer or float - 1 and 6 included


# greetings = ['Hello', 'Hi', 'Namaste', 'Howdy', 'Hola']
# value = random.choice(greetings)
# print(value)  #print single random value from list of arguments


# colors = ['Red', 'Green', 'Blue', 'Black']
# results = random.choices(colors, k=10)
# print(results)   Prints random list values specified by range in k

# colors = ['Red', 'Green', 'Blue', 'Black']
# results = random.choices(colors, weights=[18,17,2,1], k=100)
# #Greater the value in weights higher probability of number to appear
#
# print(results)   #Prints random list values specified by range in k

# deck = list(range(1,53))
# random.shuffle(deck)
# print(deck)

deck = list(range(1,53))
randomcard = random.sample(deck, k=10) #Prints unique value of card...No card value repitition
print(randomcard)

#-------------------------------------------DEMO----------------------------------------------------------------------#

''' Super simple module to create basic random data for tutorials'''

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(100):
    first = random.choice(first_names)
    last = random.choice(last_names)

    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'

    street_num = random.randint(100, 999)
    street = random.choice(street_names)
    city = random.choice(fake_cities)
    state = random.choice(states)
    zip_code = random.randint(10000, 99999)
    address = f'{street_num} {street} St., {city} {state} {zip_code}'

    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{address}\n{email}\n')