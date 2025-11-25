# ============================================================
# SUMMARY OF CLASS DEFINITION FROM claude.ai
# This code defines a **Car class** that models a car with attributes and methods:

# **Attributes (initialized in `__init__`):**
# - `make` - the car's manufacturer
# - `model` - the car's model name
# - `year` - the car's year
# - `odometer_reading` - mileage, defaults to 0

# **Methods:**

# 1. **`get_descriptive_name()`** - Returns a formatted string combining year, make,
#     and model in title case (e.g., "2019 Toyota Camry")

# 2. **`read_odometer()`** - Prints the current mileage

# 3. **`update_odometer(mileage)`** - Sets the odometer to a specific value:
#    - Accepts the change only if the new mileage is greater than or equal to the current reading
#    - Prevents rolling back the odometer (rejects lower values)

# 4. **`increment_odometer(miles)`** - Adds a specified number of miles to the current odometer reading

# **Key concepts**: 
# - Object-oriented programming with a class blueprint
# - The `self` parameter refers to the instance itself
# - Data validation in `update_odometer()` to maintain data integrity
# - Encapsulation of car data and behaviors in a single class
# ============================================================
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

    # MODIFY ATTRIBUTE VALUE THROUGH A METHOD
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# INSTANTIATE CAR OBJECT
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# MODIFYING ATTRIBUTES DIRECTLY
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# MODIFY ATTRIBUTE VALUE THROUGH A METHOD
my_new_car.update_odometer(10)
my_new_car.read_odometer()

# INCREAMENT ATTRIBUTE VALUE TRHOUGH METHOD
print("\nIncrement Funtion")
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
