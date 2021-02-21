from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import csv
from collections import Counter

# print(plt.style.available)
#
plt.style.use('seaborn-darkgrid')

# plt.xkcd()

'''with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    language_counter = Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

languages = []
popularity = []

# print(language_counter.most_common(15))

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)

#Reverses order in which data is shown
languages.reverse()
popularity.reverse()

plt.barh(languages,popularity) #barh - For Horizontal Bar

plt.title('Most Popular Languages') # Title of plot
plt.ylabel('Programming Languages') # Name of X-axis
plt.xlabel('No of Users') # Name of Y-axis


#plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.grid(True)

plt.tight_layout()
#
# plt.savefig('plot1.jpeg') #Save plot in desired image format(.jpeg,.png etc)
#
plt.show()  # Show the plot for the data'''


'''------------------------------------PANDAS------------------------------------------------------'''

data = pd.read_csv('data1.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

# print(language_counter.most_common(15))

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

# print(languages)
# print(popularity)

#Reverses order in which data is shown
languages.reverse()
popularity.reverse()

plt.barh(languages,popularity) #barh - For Horizontal Bar

plt.title('Most Popular Languages') # Title of plot
plt.ylabel('Programming Languages') # Name of X-axis
plt.xlabel('No of Users') # Name of Y-axis


#plt.legend()

# plt.xticks(ticks=x_indexes, labels=ages_x)

# plt.grid(True)

plt.tight_layout()
#
# plt.savefig('plot1.jpeg') #Save plot in desired image format(.jpeg,.png etc)
#
plt.show()  # Show the plot for the data'''















