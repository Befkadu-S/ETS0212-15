copy(): Returns a shallow copy of the set.
Example
my_set = {1, 2, 3}
copied_set = my_set.copy()
print(copied_set)  # Output: {1, 2, 3}
copied_set.add(4)
print(my_set)      # Output: {1, 2, 3} (original set is unchanged)
