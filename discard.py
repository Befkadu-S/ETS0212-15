 discard(element): Removes an element from the set if it is present. Does not raise an error if the element is not found.
Example
my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set) # Output: {1, 2, 4}
my_set.discard(5) # No error is raised
print(my_set) # Output: {1, 2, 4}
