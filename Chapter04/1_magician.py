# LOOPING THROUGH ENTIRE LIST
# CODE SUMMARY FROM claude.ai
# This code demonstrates a **for loop** that iterates through a list and performs actions for each element:

# 1. **Creates a list** of three magician names (all lowercase)

# 2. **Loops through each magician** in the list, and for each one:
#    - Prints a compliment using `.title()` to capitalize the name (e.g., "Alice, that was a great trick")
#    - Prints an anticipation message (e.g., "I cant wait to see your next trick alice")
#    - Prints a separator line of underscores

# 3. **After the loop completes**, prints a final message thanking everyone

# **Key concepts**:
# - The loop runs 3 times (once per magician)
# - The variable `magician` temporarily holds each name during its iteration
# - The two `print()` statements inside the loop are indented, so they execute for each magician
# - The final `print()` is outside the loop (not indented), so it only runs once after all iterations complete
# - `f-strings` allow embedding variables directly in strings using `{variable}` syntax

magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I cant wait to see your next trick {magician}")
    print("________________________________")

print("Thank you everyone")

# INDENTATION ERROR
# message = "Hello Python world"
#     print(message)

# FORGETTING THE COLON
# for magician in magicians
#     print(magician)

