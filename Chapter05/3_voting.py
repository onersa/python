# IF STATEMENTS
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# IF-ELIF-ELSE SATEMENTS
# OPTION 1
# =================================================================================
# CODE SUMMARY FROM calude.ai
# This code determines an admission price based on a person's age using conditional logic:
# How it works:

# Sets age to 12
# Checks three conditions in order:

# If age is less than 4: prints admission is $0
# Otherwise, if age is less than 18: prints admission is $25
# Otherwise (age 18 or older): prints admission is $40



# In this example: Since age is 12, it skips the first condition (12 is not less than 4), matches the second condition (12 is less than 18), and outputs: "Your admission cost is $25."
# This is a common pricing structure where children get in free, minors pay a reduced rate, and adults pay full price
# =================================================================================
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    
    

#  OPTION 2
age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 25
else:
 price = 40
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
else:
 price = 20
print(f"Your admission cost is ${price}.")

# TEST MULTIPLE CONDITIONS
# ===========================================================================================================================
# SUMMARY FROM claude.ai
# This code demonstrates the difference between independent if statements and if-elif chains in Python:
# First block (lines 65-72): Uses separate if statements

# Checks the list for mushrooms → prints "Adding mushrooms"
# Checks for pepperoni → finds nothing, skips
# Checks for extra cheese → prints "Adding extra cheese"
# Result: Both toppings get added because each condition is evaluated independently

# Second block (lines 74-80): Uses if-elif-elif chain

# Checks for mushrooms → prints "Adding mushrooms"
# Stops checking after the first match (that's how elif works)
# Result: Only mushrooms get added, extra cheese is ignored

# So it's a teaching example showing that:

# Multiple ifs = check everything, execute all matches
# if-elif chain = stop at first match, execute only one block

# The pizza ends up with different toppings depending on which approach you use! 🍕
# ===============================================================================================================================
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
 if requested_topping == 'green peppers':
    print("Sorry, we are out of green peppers right now.")
 else:
     print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")