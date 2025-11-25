# # Store information about a pizza being ordered.
# pizza = {
#  'crust': 'thick',
#  'toppings': ['mushrooms', 'extra cheese'],
#  }
# # Summarize the order.
# print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
# for topping in pizza['toppings']:
#  print(f" 🍕 {topping}")

# ==========================================
# SUMMARY OF CDE FROM calude.ai
# This code demonstrates working with a dictionary where each value is a list:

# 1. It creates a dictionary `favorite_languages` where each key is 
# a person's name and each value is a list of their favorite programming languages

# 2. It loops through the dictionary using `.items()` to get both the name (key) and languages (value list) for each person

# 3. For each person, it prints their name in title case followed by "favorite languages are:"

# 4. It then has a nested loop that iterates through each language in 
# that person's list and prints each one indented with a tab (`\t`) and in title case

# The code shows how to iterate through nested data structures (a dictionary containing lists).
# ===========================================
favorite_languages = {
'jen': ['python', 'rust'],
'sarah': ['c'],
'edward': ['rust', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
   print(f"\n{name.title()}'s favorite languages are:")
   for language in languages:
      print(f"\t{language.title()}")