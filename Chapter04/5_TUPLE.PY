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
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
