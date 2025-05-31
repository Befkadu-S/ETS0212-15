index(value[, start[, end]]): The index() method is used to find the first occurrence of a specified value within a tuple. You can also specify optional start and end indices to limit the search to a specific section of the tuple.
Example
my_tuple = (1, 2, 3, 2, 4)

# Find the index of the first occurrence of '3'
index_of_three = my_tuple.index(3)  
print(index_of_three)  # Output: 2

# Find the index of '2', starting the search from index 3
index_of_two_after_index_3 = my_tuple.index(2, 3)  
print(index_of_two_after_index_3)  # Output: ValueError, because '2' does not appear after index 3
