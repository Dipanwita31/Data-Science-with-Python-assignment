a=int(input("Enter 1st Subject number: "))
b=int(input("Enter 2nd Subject number: "))
c=int(input("Enter 3rd Subject number: "))
d=int(input("Enter 4th Subject number: "))
e=int(input("Enter 5th Subject number: "))
total=a+b+c+d+e
per=(total/500)*100
if(total<=500 and total>=420):
    print("Pass \n Divison:1st \n percentage:",per)
elif(total<=419 and total>=200):
    print("Pass \n Divison:2nd \n percentage:",per)
elif(total<=199 and total>=100):
    print("Pass \n Divison:2nd \n percentage:",per)
else:
    print("Fail")
    
    
