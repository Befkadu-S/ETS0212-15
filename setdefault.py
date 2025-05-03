 setdefault(): If the key exists, returns its value. If not, inserts the key with a specified value (optional, defaults to None) and returns that value.
Example
my_dict = {"a": 1, "b": 2}
value = my_dict.setdefault("b", 5) # Key exists, value unchanged
print(value)    # Output: 2
print(my_dict) # Output: {'a': 1, 'b': 2}

value = my_dict.setdefault("c", 3) # Key doesn't exist, inserted with value 3
print(value)    # Output: 3
print(my_dict) # Output: {'a': 1, 'b': 2, 'c': 3}
