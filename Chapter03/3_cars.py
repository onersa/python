# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() #we are doing the sort method 
# print(cars)

# cars.sort(reverse=True)
# print(cars)

#SORTING LIST TEMPORARILY WITH SORTED() METHOD
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("\nOriginal List: {cars}")

# sorted_cars = sorted(cars)

# print(f"\n1) Sorted List: {cars}")
# print(f"After Sorted List: {sorted_cars}")

# print("\n")

#PRINTING A LIST IN REVERSE ORDER
# This code has an issue. Here's what's happening:
# The problem:

# cars.sort() sorts the list in-place (modifies the original list) but returns None
# So print(cars.sort()) prints None instead of the sorted list

# To fix it, use one of these approaches:
# Option 1: Sort first, then print
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Reversed List = {cars.sort()}")

# REVIEWED CODE TO DEAL WITH THE RERUTN None FROM ABOVE
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(f"Reversed List = {cars.sort()}")



#FINDING LENGTH OF A LIST
print(f"\nLength of cars list = {(len(cars))}")