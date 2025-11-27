k=0
numbers=[]
positive=[]
n=int(input("Enter the number of elements in the integer list:\n"))
for i in range(n):
    value = int(input(f"Enter value {i+1} of list:\n"))
    numbers.append(value)

for i in range(n):
    if numbers[i]>0:
        positive.append(numbers[i])
        k+=1

print("Positive values are:\n")
for i in range(k):
    print(positive[i])
