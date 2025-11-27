list1=[]
list2=[]

max_count=int(input("Enter number of values to insert:\n"))

for _ in range(max_count):
    value=int(input("Enter value:\n"))
    list1.append(value)

for num in list1:
    if num % 2 != 0:
        list2.append(num)

print("Removed even values:\n")
for num in list2:
    print(num)
