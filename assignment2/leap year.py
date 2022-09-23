n=int(input("Enter the year: "))
if n%400==0:
    if n%4==0:
        print("The year is leap year")
    else:
        print("The year is not leap year")
else:
     if n%100!=0:
         print("The year is leap year")
     else:
         print("The year is not a leap year")
