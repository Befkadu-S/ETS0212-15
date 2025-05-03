 copy(): Returns a shallow copy of the dictionary.
Example
my_dict = {"a": 1, "b": 2, "c": 3}
new_dict = my_dict.copy()
new_dict["d"] = 4 # Modifying the copy doesn't affect the original
print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3}
print(new_dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
