a=1000
for i in range(0,a,1):
    s=0
    temp=i
    while temp>0:
        digit=temp%10
        s+=digit**3
        temp//=10
    if i==s:
        print(i)
