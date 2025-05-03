update(): Updates the dictionary with the key-value pairs from another dictionary or iterable of key-value pairs.
Example
my_dict = {"a": 1, "b": 2}
my_dict.update({"c": 3, "d": 4})
print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_dict.update([("e", 5), ("f", 6)]) # Using a list of tuples
print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
