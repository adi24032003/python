a=int(input("Enter first value: "))
b=int(input("Enter second value: "))

while b!=0:
    temp=a
    a=b
    b=temp % b

print("The GCD is:", a)
