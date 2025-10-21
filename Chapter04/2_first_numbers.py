# NUMERICAL LISTS
# USING RANGE FUNCTION
for value in range(1,5):
    print(value)

numbers = list(range(1,5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)

# STATS
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# squares = list(value ** 2 for value in range(1,11))
squares = [value ** 2 for value in range(1,11)]
print(f"Squares: {squares}")