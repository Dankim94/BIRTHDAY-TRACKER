import calendar #Adding libraries to have access to calendar
from icalendar import Calendar, Event #Adding libraries to have access to calendar and event 
import datetime #Adding libraries to have access to date and time
year = input("Enter the year of birth: ") #Enter the year of the birth
year = int(year)
print(calendar.calendar(year)) #show the calendar of the year of birth
now = datetime.datetime.now()
print(now) #get the current date and time


calendar = Calendar()
calendar.add('prodid', '-//My calendar product//example.com//')
calendar.add('version', '2.0')
event = Event()
type_event = input("Enter the type of event (birthday, anniversary, etc.): ") #Enter the type of event
input_event = input("Enter the event name: ") #Enter the event name
event.add(type_event, input_event)

with open('my_calendar.ics', 'wb') as f: #Create a new calendar file
    f.write(calendar.to_ical()) #Write the calendar to the file

with open('my_calendar.ics', 'rb') as f: #Open the calendar file
    calendar = Calendar.from_ical(f.read()) #Read the calendar from the file








