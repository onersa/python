## CAR RENTAL
# car = input("What car do you want? ")
# message = f"Let me see if I can find you a {car}"
# print(message)

## RESTAURENT SEEATING
# num_of_guests = int(input("How many are you? "))
# # num_of_guests = int(num_of_guests)

# if num_of_guests > 8:
#     print(f"We do not have a table to accommodate {num_of_guests} guests!")
# else:
#     print(f"Reservation is confirmed for {num_of_guests} guests!")

# MULTIPLES OF 10
# ===================================================
# SUMMARY FROM claude.ai
# This code checks whether a number is a **multiple of 10**:

# 1. **Prompts the user** to enter a number and converts the input to an integer using `int()`

# 2. **Uses the modulo operator (`%`)** to check divisibility:
#    - `num % 10` calculates the remainder when `num` is divided by 10
#    - If the remainder equals 0, the number is a multiple of 10

# 3. **Prints the result**:
#    - **If `num % 10 == 0`**: confirms the number is a multiple of 10
#    - **Otherwise**: states the number is not a multiple of 10

# **Key concept**: The modulo operator (`%`) returns the remainder of division. 
# Any number that divides evenly by 10 (like 20, 50, 100) will have a remainder of 0,
# while numbers like 23 or 47 will have non-zero remainders.
# ===================================================
num = int(input("Please type in any number: "))

if num % 10 == 0 :
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of ten")


