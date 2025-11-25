# ===============================================================================================# 
# SUMMARY OF CODE BELOW
# This code demonstrates a **while loop for collecting user input** until a specific condition is met:

# 1. **Creates a multi-line prompt** using string concatenation (`+=`):
#    - Asks user to enter pizza toppings
#    - Instructs them to type "quit" when finished

# 2. **Initializes** `toppings` variable as an empty string

# 3. **Runs a loop** that continues until the user types "quit" (case-insensitive):
#    - Prompts for and receives a topping from the user
#    - **If the input is NOT "quit"**: prints a confirmation message
#      with the topping in uppercase

# 4. **Loop exits** when user enters "quit" (in any case: quit, QUIT, Quit, etc.)

# **Key concepts**:
# - `.lower()` method converts input to lowercase for case-insensitive comparison
# - `.upper()` method displays the topping in uppercase in the confirmation
# - The nested `if` statement prevents printing "quit" as a topping
# - The loop condition checks before processing, 

# but input happens inside the loop, so "quit" is read but not processed as a topping
# ====================================================================================
# WHILE LOOP EXAMPLE
prompt = "\nEnter the toppings for your pizza." 
prompt += "\nPlease enter quit when done. "

toppings = ""

while toppings.lower() != "quit":
    toppings = input(prompt)
    if toppings != "quit":
        print(f"The {toppings.upper()} topping has been added to your pizza")
