# NUMERICAL LISTS
# USING RANGE FUNCTION
# for value in range(1,5):
#     print(value)

# numbers = list(range(1,5))
# print(type(numbers))
# print(numbers)

# even_numbers = list(range(2, 11,2))
# print(even_numbers)

# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)

# print(squares)

# STATS
# CODE SUMMARY FROM clause.ai
# This code demonstrates basic Python list operations:
# Creates a list of single digits (1-9 and 0)
# Prints the original list as-is
# Prints a separator line of underscores
# Prints the sorted list - arranges digits in ascending order (0-9)
# Prints the minimum value - finds the smallest number (0)
# Prints the maximum value - finds the largest number (9)
# Prints the sum - adds all digits together (45)
# The code showcases built-in Python functions (sorted(), min(), max(), sum()) that work with lists.

digits = [1, 8, 2, 7, 5, 6, 4, 3, 9, 0]

print("_________________________________")
print(f"Sorted digits: {sorted(digits)}")
print(f"minimum value: {min(digits)}")
print(f"maximum value: {max(digits)}")
print(f"sum of all digits: {sum(digits)}")

# squares = list(value ** 2 for value in range(1,11))
# using a list comprehension
print("_________________________________")
squares = [value ** 2 for value in range(1,11)]
print(f"Squares: {squares}")

