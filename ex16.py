from datetime import datetime, timedelta
import calendar

now=datetime.now()

testDate=now+timedelta(days=2)
myFirstMeetUp=now-timedelta(weeks=3)

print(f"My first test date is: {testDate.date()}")
print(myFirstMeetUp.date())

if testDate > myFirstMeetUp:
    print("It works")

cal=calendar.month(1998,9)
print(cal)

cal2=calendar.weekday(1998,9,23)
print(cal2)

