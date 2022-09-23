num1= int(input("Please enter the first number: "))
num2= int(input("Please enter the second number: "))

mn = min(num1, num2)

for i in range(1, mn+1):

    if num1%i==0 and num2%i==0:
        c = i
    
if c == 1:
    print("They are Co-Prime.")

else:
    print("They are not Co-Prime.")
