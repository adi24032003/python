full_names=["Rabah Ahmed", "Sandhul mk", "Shahal PK"]
first_names=[]
for name in full_names:
    first_names.append(name.split()[0])

count=0
for name in first_names:
    count+=name.lower().count('a')

print(count)
