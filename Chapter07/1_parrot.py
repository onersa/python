prompt = "\nTell me something and I will speak it back to you"
prompt  += "\nEnter 'quit' to end the program. "

message  = ""

# while message.lower() != "quit":
#     message = input (prompt)
#     print(message)

#WHILE USING A FLAG
# =============================================================
# SUMMARY OF THE CODE SNIPPET
# This code demonstrates a **while loop with a flag variable** to control program execution:

# 1. **Sets a flag variable** `active` to `True` to control the loop

# 2. **Runs a continuous loop** that keeps executing as long as `active` is `True`:
#    - Prompts the user for input and stores it in `message` 
#      (note: `prompt` variable is used but not defined in this snippet)
#    - **If the user types 'quit'**: sets `active` to `False`, 
#      which will end the loop on the next iteration
#    - **Otherwise**: prints back whatever the user typed

# 3. **Loop exits** when the user enters 'quit'

# **Key concepts**: 
# - Using a boolean flag to control loop execution (cleaner than using `break` statements)
# - The `input()` function pauses and waits for user input
# - The code has a small issue: `prompt` is referenced but never defined, 
# which would cause an error unless it was defined earlier in the full program
# =============================================================
active = True

while active:
 message = input(prompt)
 if message == 'quit':
    active = False
 else:
    print(message)