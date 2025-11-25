# RETURNING A DICTIONARY
# EXAMPLE 1
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name.title(), 'last': last_name.title()}
    
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# EXAMPLE 2
# ============================================================
# This code demonstrates a **function with optional parameters** that returns a dictionary:

# 1. **Defines a function** `build_person()` that takes three parameters:
#    - `first_name` and `last_name` (required)
#    - `age` (optional, defaults to `None`)

# 2. **Creates a dictionary** with the person's first and last name

# 3. **Conditionally adds age**:
#    - If an age value is provided (truthy), it adds an `'age'` key to the dictionary
#    - If age is `None` or not provided, the dictionary only contains name fields

# 4. **Returns the dictionary** containing the person's information

# 5. **Calls the function** with all three arguments (`'jimi'`, `'hendrix'`, `age=27`)

# 6. **Prints the result**: `{'first': 'jimi', 'last': 'hendrix', 'age': 27}`

# **Key concepts**:
# - Default parameter values (`age=None`) make arguments optional
# - The function builds and returns a data structure (dictionary)
# - Conditional logic determines which keys are included in the returned dictionary
# - Using keyword arguments (`age=27`) improves code readability
# ============================================================
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age

    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

musician = build_person('jimi', 'hendrix')
print(musician)

musician = build_person('jimi', 'hendrix', 27)
print(musician)