nums=[int(x) for x in input("Enter numbers:").split()]
result=[]
for x in nums:
    if x>100:
        result.append("over")
    else:
        result.append(x)
print(result)

