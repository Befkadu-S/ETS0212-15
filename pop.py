pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
Example
my_set = {1, 2, 3}
removed_element = my_set.pop()
print(removed_element) # Output: (One of 1, 2, or 3 - the order is not guaranteed)
print(my_set)       #Output: A set with the remaining elements
