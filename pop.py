pop(): Removes and returns the item with the specified key. Raises a KeyError if the key doesn't exist (unless a default is provided).
Example
my_dict = {"a": 1, "b": 2, "c": 3}
value = my_dict.pop("b")
print(value)      # Output: 2
print(my_dict)   # Output: {'a': 1, 'c': 3}

value = my_dict.pop("d", "Not Found") # Provide default value to avoid KeyError
print(value) # Output: Not Found


