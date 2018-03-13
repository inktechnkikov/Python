import  datetime
import calendar

def printDate():
    today = datetime.date.today()
    print(today)

def isLeapYear():
    getYear = int(input())
    print(calendar.isleap(getYear))

isLeapYear()