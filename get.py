get(): Returns the value of the specified key.
Example
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.get("b"))   # Output: 2
print(my_dict.get("d"))   # Output: None
print(my_dict.get("d", 0)) # Output: 0 (using a default value)

