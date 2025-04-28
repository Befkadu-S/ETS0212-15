keys = ("apple", "banana", "cherry")
value = 0
my_dict = dict.fromkeys(keys, value)
print(my_dict) # Output: {'apple': 0, 'banana': 0, 'cherry': 0}

my_dict = dict.fromkeys(keys) # Value defaults to None
print(my_dict) # Output: {'apple': None, 'banana': None, 'cherry': None}

