# READING CONTENTS OF A FILE
# =========================================================
# SUMMARY FROM claude.ai
# This code demonstrates **reading and processing a text file** using the `pathlib` module:

# 1. **Imports necessary modules**:
#    - `Path` from `pathlib` for file handling
#    - `math` (imported but not used in this snippet)

# 2. **Creates a Path object** pointing to "pi_digits.txt"

# 3. **Reads the entire file** into a string using `.read_text()`

# 4. **Prints the contents** with `.rstrip()` to remove trailing whitespace/newlines

# 5. **Splits content into lines**:
#    - `.splitlines()` breaks the string into a list where each element is one line
#    - Removes the newline characters in the process

# 6. **Loops through and prints each line** individually

# 7. **Prints the entire list** of lines to show the list structure

# **Key concepts**:
# - Modern file reading with `pathlib` (cleaner than traditional `open()`)
# - `.read_text()` reads the entire file as a single string
# - `.splitlines()` converts multi-line text into a list for line-by-line processing
# - The code demonstrates two ways to view the data: as formatted lines and as a list structure

# =========================================================

from pathlib import Path

import math

path =  Path("pi_digits.txt")
contents = path.read_text()
print(contents.rstrip())

# WORKING WITH FILE CONTENTS
lines = contents.splitlines()
for line in lines:
    print(line)
print(lines)    

pi_string = ""
for line in lines:
    pi_string += line.lstrip() # removes the left space from the 2nd and 3rd lines from the file
    
    
print(pi_string)
print(len(pi_string))


path =  Path("pi_ten_million.txt")
contents = path.read_text()

pi_string = contents.splitlines()
print(pi_string[:52])
