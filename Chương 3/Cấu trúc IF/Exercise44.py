month=input("Enter the month: ")
day=int(input("Enter the day: "))

if month=="January" and day==1:
    print("New Year's Day")
elif month=="July" and day==1:
    print("Canada Day")
elif month=="December" and day==25:
    print("Christmas Day")
else:
    print("The entered month and day do not correspond to a fixed-date holiday!")
