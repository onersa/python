age = 18
print(f"Is the person 18 years old?: {age == 18}")

age = 19
print(f"Is the person below 21 years of age?: {age < 21}")
print(f"Is the person  21 years old or younger?: {age <= 21}")

print(f"Is the person above 21 years of age?: {age > 21}")
print(f"Is the person at least 21 years of age?: {age >= 21}")


# CHECKING MULTIPLE CONDITIONS
# 1) USING AND OPERATOR
age_0 = 22
age_1 = 18
admission = age_0 >= 21 and age_1 >= 21
print(f"Are both patrons allowed to purchase?: {admission}")
age_1 = 22
admission = age_0 >= 21 and age_1 >= 21
print(f"Can the watch the movies?: {admission}")

# CHECKING WHETHER A VALUE IS IN A LIST
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print(f"Add mushrooms for order{'mushrooms' in requested_toppings}")
print(f"Add pepperoni for order{'pepperoni' in requested_toppings}")

# CHECKING WHETHER A VALUE IS NOT IN A LIST
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
 print(f"{user.title()}, you can post a response if you wish.")
else:
 print(f"{user.title()}, you are not authorised to access this site")

#  BOOLEAN EXPRESSION

 
