dict1={'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
sorted_dict_asc=dict(sorted(dict1.items()))
print("Ascending order:",sorted_dict_asc)
sorted_dict_dec= dict(sorted(dict1.items(), reverse=True))
print("Descending order:",sorted_dict_dec)

