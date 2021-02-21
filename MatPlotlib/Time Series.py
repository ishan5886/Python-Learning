import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#
# y = [0, 1, 3, 4, 6, 5, 7]
#
# plt.plot_date(dates,y, linestyle='solid')
#
# plt.gcf().autofmt_xdate() #Autoformat dates
#
# date_format = mpl_dates.DateFormatter('%b, %d, %Y')
#
# plt.gca().xaxis.set_major_formatter(date_format)  #Set date according to specific format

# Datetime formatting codes URL :- http://bit.ly/python-dt-fmt

data = pd.read_csv('datatimeseries.csv')

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)  #inplace repales data=data.sort

price_date = data['Date']
price_close = data['Close']


plt.plot_date(price_date,price_close, linestyle='solid')
plt.gcf().autofmt_xdate()


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')



plt.tight_layout()
plt.show()