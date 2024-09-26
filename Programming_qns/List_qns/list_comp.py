'''
elif in list comp


Python's conditional expressions were designed exactly for this sort of use-case:

>>> l = [1, 2, 3, 4, 5]
>>> ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]
['yes', 'no', 'idle', 'idle', 'idle']

'''
l = [0,1, 2, 3, 4, 5]
[print('yes',end=',') if i == 1 else print('zero',end=',') if i ==0 else print('no',end=',')for i in l ]
print(l)

# List comprehensions in Python provide a concise and readable way to create lists. 
# They are a syntactic construct that allows you to create a list based on an existing 
# iterable, applying an expression to each element and optionally filtering the elements.

#  Here are some examples:

# Examples of List Comprehensions:
# Create a list of squares:
squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

# Filter even numbers:

even_numbers = [x for x in range(10) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8]
# Convert strings to uppercase:

# python
# Copy code
words = ["hello", "world", "python", "developer"]
filtered_upper = [word.upper() for word in words if "o" in word]
print(filtered_upper)  # ['HELLO', 'WORLD', 'PYTHON']

# Create a list of tuples:

# python
# Copy code
pairs = [(x, x*2) for x in range(3)]
# # Output: [(0, 0), (1, 2), (2, 4)]
# When to Use List Comprehensions:
# Simple Transformations and Filtering:

# Use list comprehensions when you need to create a new list by applying a simple transformation or filtering elements based on a condition. They make the code concise and expressive.
# Readability:

# Use list comprehensions when they enhance readability and make the code more compact without sacrificing clarity. However, avoid overly complex comprehensions that may reduce readability.
# Avoid Repetition:

# Use list comprehensions to avoid repetitive code that would be present in a traditional for loop.
# When Not to Use List Comprehensions:
# Complex Logic:

# Avoid using list comprehensions for complex logic that might make the comprehension difficult to understand. 
# In such cases, it's better to use a traditional for loop.

# Side Effects:

# If the expression in the list comprehension has side effects, such as modifying variables outside the comprehension, 
# it's better to use a regular for loop for clarity.
# Nested Comprehensions:

# Avoid excessive nesting of list comprehensions, as it can reduce readability. If the logic becomes too complex,
# consider breaking it into separate steps or using traditional loops.
# Debugging:

# When debugging is needed, a traditional for loop may be more suitable as it allows for easier insertion of print statements or breakpoints.
# In summary, list comprehensions are a powerful and concise tool in Python, suitable for simple transformations and filtering operations. 
# However, it's essential to balance conciseness with readability and avoid unnecessary complexity. In cases where clarity is sacrificed,
#  or when dealing with more complex logic, using a traditional for loop might be preferable.