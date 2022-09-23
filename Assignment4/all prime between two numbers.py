s = int(input("enter start no"))
n = int(input("Enter end no:"))
for num in range(s, n+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
