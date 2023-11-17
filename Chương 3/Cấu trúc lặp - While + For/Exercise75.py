a=int(input("Enter the positive integer: "))
b=int(input("Enter the positive integer: "))
m=min(a,b)

while a%m!=0 or b%m!=0:
    m=m-1

print("The greatest common divisor of",a,"and",b,"is",m)
