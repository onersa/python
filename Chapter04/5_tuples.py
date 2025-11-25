# IMMUTABLE UNCHANGEABLE LIST
dimensions = (200,50) # dimensions = 200,50
print(dimensions[0])
print(dimensions[1])

# ERROR IMMUTABLE: TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 10

print("Original dimensions:")
for dimension in dimensions:
 print(dimension)
 
# CAN REASSIGN THE ENTIRE TUPLE
# This code demonstrates working with a **tuple** - an immutable (unchangeable) sequence in Python:

# 1. **Creates a tuple** containing two values: `400` and `100`
#    - Tuples use parentheses `()` instead of square brackets like lists
#    - Unlike lists, tuples cannot be modified after creation

# 2. **Prints a header** with a newline character (`\n`) before the text

# 3. **Loops through the tuple** and prints each dimension value on a separate line:
#    - First iteration prints `400`
#    - Second iteration prints `100`

# **Key concept**: Despite the header saying "Modified dimensions:", 
# the tuple itself isn't actually being modified in this code - it's just being iterated over and displayed. 
# The name is likely misleading or part of a larger example where the tuple was
# reassigned (you can reassign the entire tuple variable, but you can't change individual elements within it).
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
