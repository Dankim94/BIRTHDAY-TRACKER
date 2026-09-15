import calendar 
import datetime
year = input("Enter the year of birth: ")
year = int(year)
print(calendar.calendar(year))
now = datetime.datetime.now()
print(now)


