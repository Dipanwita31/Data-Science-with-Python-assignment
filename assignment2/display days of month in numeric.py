print("January=1,February=2,march=3,april=4,may=5,june=6,july=7,august=8,september=9,october=10,november=11,december=12")
a=int(input("enter a no of correct month"))
if(a==2):
    print("no of days is 28")
elif a in(4,6,9,11):
    print("no of day is 30")
elif a in(1,3,5,7,8,10,12):
    print("no of days is 31")
else:
    print("wrong input")
