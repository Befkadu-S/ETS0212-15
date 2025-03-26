upper(): Converts all characters in the string to uppercase.

Example 

text = "hello"
print(text.upper())  # Output: "HELLO"

lower(): Converts all characters in the string to lowercase.

Example 

text = "HELLO"
print(text.lower())  # Output: "hello"

replace(): Replaces a specified substring with another substring.

Example 

text = "I like cats"
new_text = text.replace("cats", "dogs")
print(new_text)  # Output: "I like dogs"


second commit

strip(): Removes leading and trailing whitespace characters (spaces, tabs, newlines).

Example

text = "  Hello World  "
print(text.strip())  # Output: "Hello World"

split(separator): Splits the string into a list at each occurrence of the separator.

Example

text = "Hello World Python"
print(text.split())  # Output: ['Hello', 'World', 'Python']

join(iterable): Joins the elements of an iterable (like a list) into a string with a specified separator.

Example 

words = ['Hello', 'World', 'Python']
print(" ".join(words))  # Output: "Hello World Python"





