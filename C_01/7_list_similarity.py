list1=[int(x) for x in input("Enter first list: ").split()]
list2=[int(x) for x in input("Enter second list: ").split()]
if len(list1)==len(list2):
    print("bot lists are of same length")
else:
    print("Lists are of different lengths")
if sum(list1)==sum(list2):
    print("Both lists sum to the same value")
else:
    print("Lists sum to different values")
common=set(list1) & set(list2)
if common:
    print("Common values:",common)
else:
    print("No common values")
