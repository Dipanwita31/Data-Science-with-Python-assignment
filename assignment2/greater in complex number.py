a=int(input("enter the 1st part"))
b=int(input("enter the 2nd part"))
c=complex(a,b)
print(c)
print(c.real)
print(c.imag)
if(c.real>c.imag):
    print("the greater no is",c.real)
else:
    print("the greater no is:",c.imag)

