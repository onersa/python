# #  MODIFYING ELEMENTS IN A LIST
# motocycles = ["honda","yamaha", "suzuki"]
# print(motocycles)

# motocycles[0] = "ducati"
# print(motocycles)

#  APPENDING AN ELEMEN ITO THE END OF LIST
# motocycles = ["honda","yamaha"]
# motocycles.append("suzuki")
# print(motocycles)

# motocycles.insert(0,"ducati")
# print(motocycles)

# REMOVING ELEMENTS FROM THE LIST
# del motocycles[1]
# print(motocycles)
# popped_item = motocycles.pop()
# print(popped_item)
# print(motocycles)

# popped_item_first = motocycles.pop(0)
# print(popped_item_first)
# print(motocycles)

#  REMEOVE ITEM FROM THE LIST  BY NAME
# motocycles = ["ducati","honda","yamaha", "suzuki"]

# motocycles.remove("honda")
# print(motocycles)
# too_expensive = "ducati"
# motocycles.remove(too_expensive)
# print(too_expensive)
# print(motocycles)

# SORT ITEMS IN THE LIST
# cars = ["toyota", "subaru", "bmw", "audi"]
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# SORTED LIST TEMPORARILY WITH SORTED() METHOD
# cars = ["toyota", "subaru", "bmw", "audi"]
# print(sorted(cars))
# print(cars) # original list not sorted

# cars = [ "audi", "toyota", "subaru", "bmw"]
# sorted_cars = sorted(cars, reverse=True)
# print(cars)
# print(sorted_cars)

#  PRINT ITEMS IN REVERSE ORDER (NOT ALPHABETIC ORDERING)
cars = [ "audi", "toyota", "subaru", "bmw"]
print(cars)
cars.reverse()
print(cars)

#  FIND THE LENGTH OF LIST
print((f"length of the list: {len(cars)}"))

cars.insert(22, "tesla")
print(cars)