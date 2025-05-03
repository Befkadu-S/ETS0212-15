 popitem(): Removes and returns the last inserted key-value pair (as a tuple) in versions 3.7 and later. In earlier versions, it removes and returns an arbitrary key-value pair.
Example
my_dict = {"a": 1, "b": 2, "c": 3}
value = my_dict.pop("b")
print(value)      # Output: 2
print(my_dict)   # Output: {'a': 1, 'c': 3}
value = my_dict.pop("d", "Not Found") # Provide default value to avoid KeyError
print(value) # Output: Not Found


