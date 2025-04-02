str.lower() – Converts all characters in the string to lowercase.
text = "Hello World"
print(text.lower())  # Output: "hello world"

str.upper() – Converts all characters in the string to uppercase.
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"

str.title() – Capitalizes the first letter of each word.
text = "hello world"
print(text.title())  # Output: "Hello World"

str.capitalize() – Capitalizes only the first letter of the string.
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

str.swapcase() – Swaps uppercase to lowercase and vice versa.
text = "Hello World"
print(text.swapcase())  # Output: "hELLO wORLD"

str.find(substring) – Returns the index of the first occurrence of the substring, or -1 if not found.
text = "Hello world"
print(text.find("world"))  # Output: 6

str.index(substring) – Like find(), but raises an error if the substring is not found.
text = "Hello world"
print(text.index("world"))  # Output: 6

str.startswith(substring) – Checks if the string starts with a given substring.
text = "Hello world"
print(text.startswith("Hello"))  # Output: True

str.endswith(substring) – Checks if the string ends with a given substring.
text = "Hello world"
print(text.endswith("world"))  # Output: True

str.count(substring) – Counts occurrences of a substring.
text = "banana"
print(text.count("a"))  # Output: 3

str.replace(old, new) – Replaces occurrences of a substring with another string.
text = "Hello world"
print(text.replace("world", "Python"))  # Output: "Hello Python"

str.strip() – Removes whitespace (or specified characters) from both ends.
text = "  Hello world  "
print(text.strip())  # Output: "Hello world"

str.lstrip() – Removes whitespace (or specified characters) from the left side.
text = "  Hello world  "
print(text.lstrip())  # Output: "Hello world  "

str.rstrip() – Removes whitespace (or specified characters) from the right side.
text = "  Hello world  "
print(text.rstrip())  # Output: "  Hello world"

str.split(separator) – Splits a string into a list of substrings.
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

str.join(iterable) – Joins elements of an iterable into a string.
words = ["Hello", "world"]
print(" ".join(words))  # Output: "Hello world"

str.isalpha() – Checks if the string consists of only letters.
text = "Hello"
print(text.isalpha())  # Output: True

str.isdigit() – Checks if the string consists of only digits.
text = "123"
print(text.isdigit())  # Output: True

str.isalnum() – Checks if the string consists of only letters and/or digits.
text = "Hello123"
print(text.isalnum())  # Output: True

str.isspace() – Checks if the string consists of only whitespace.
text = "   "
print(text.isspace())  # Output: True

str.format() – Formats a string with placeholders.
text = "My name is {} and I am {} years old."
print(text.format("Alice", 25))  # Output: "My name is Alice and I am 25 years old."

F-strings (f"{value}") – A modern way to format strings in Python.
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  # Output: "My name is Alice and I am 25 years old."

len(str) – Returns the length of the string.
text = "Hello"
print(len(text))  # Output: 5

str.encode() – Encodes a string into bytes.
text = "Hello"
print(text.encode())  # Output: b'Hello'

str.islower() – Checks if all letters in the string are lowercase.
text = "hello"
print(text.islower())  # Output: True

str.isupper() – Checks if all letters in the string are uppercase.
text = "HELLO"
print(text.isupper())  # Output: True