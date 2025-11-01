cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# check for equality
car = "bmw"
print(f"Car: {car}")
print(f"Is the car a bmw {car == 'bmw'}")
car = "audi"
print(f"Car: {car}")
print(f"Is the car a bmw {car == 'bmw'}")

#CASE SENSITIVITY
car = "Audi"
print(f"Car: {car}")
print(f"Car: {car}")
print(f"Is the car a Audi {car == 'audi'}")
print(f"Is the car a Audi {car.lower() == 'audi'}")

# CHECK INEQUALITY
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")