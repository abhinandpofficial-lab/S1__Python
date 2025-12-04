my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
ascending_dict = dict(sorted(my_dict.items()))
print("Ascending is:", ascending_dict)
descending_dict = dict(sorted(my_dict.items(), reverse=True))
print("Descending is:", descending_dict)