import calendar 
import datetime #Adding libraries to have access to calendar and datetime functions 
year = input("Enter the year of birth: ") #Enter the year of the birth
year = int(year)
print(calendar.calendar(year)) #show the calendar of the year of birth
now = datetime.datetime.now()
print(now) #get the current date and time
event = input("Enter the event: ")
print(event) #have access to an event that the user want to add to the calendar



