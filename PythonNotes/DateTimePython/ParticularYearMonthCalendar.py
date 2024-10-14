import calendar
year=int(input("Enter Year number:"))
month=int(input("Enter month number:"))

cal = calendar.month(year, month)
print ("Here is the calendar of ")
print (cal)


y=int(input("Enter Year:"))
cal = calendar.calendar(y)
print(cal)