from matplotlib import pyplot as plt
import numpy as np


# print(plt.style.available)
#
plt.style.use('seaborn-darkgrid')

# slices = [60,40, 30,20]
# labels = ['Sixty', 'Forty', 'Thirty', 'Twenty']
# colors = ['blue', 'red', 'yellow', 'green']

# Language Popularity
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++',
#           'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']


slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]


# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=180, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})


plt.title('My Pehla Pie Chart') # Title of plot
plt.tight_layout()
plt.show()  # Show the plot for the data