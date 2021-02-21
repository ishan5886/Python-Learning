import datetime  #imports datetime module

# d = datetime.date(2016, 7, 24)   #yyyy, m, dd
# print(d)  #date format printed yyyy-mm-dd

# tday =  datetime.date.today()  #print today's date
# # print(tday)  # print today's date
# # print(tday.year) # print year
# # print(tday.month)  # print month
# # print(tday.day)  # print month
# #
# # print(tday.weekday()) # print index of current weekday (index start from 0)
# # print(tday.isoweekday()) # print index of current weekday (index start from 1)
# tdelta = datetime.timedelta(days=7)
# print(tday + tdelta)   Print date 7 days from tday date


# t = datetime.time(9, 30, 45, 100000)  # h,mm, ss, milliseconds
# print(t)  #time format printed hh:mm:ss.milliseconds

# dt = datetime.datetime(2016, 7, 26,9, 30, 45, 100000)
# print(dt)  #print full datetime
# print(dt.time()) #print only time
# print(dt.year)
# print(dt.hour)
# print(dt.month)
import pytz as pytz

# dt_today =  datetime.datetime.today()
# dt_now =  datetime.datetime.now()
# dt_utcnow =  datetime.datetime.utcnow()
#
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2016, 7, 26,9, 30, 45, tzinfo=pytz.UTC)
# print(dt) print UTC offset

# dt_now =  datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

dt_ist = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))  #prints local IST timezone time
# print(dt_ist)
#
# for tz in pytz.all_timezones:    # prints all timezones present in pytz package
#     print(tz)
#
# # dt_utcnow =  datetime.datetime.utcnow()
# # print(dt_utcnow)

# dt_naive = datetime.datetime.now()
# ist_tz = pytz.timezone('Asia/Kolkata')
# dt_naive = ist_tz.localize(dt_naive)
# print(dt_naive)


print(dt_ist.strftime('%B %d, %Y ')) #Print time based on pattern codes