# strings.py

# Task 1: String Manipulation
# ---------------------------
# 1. Concatenate the following strings: "Python", " is", " awesome!"
print("Python"+" is"+" awesome!")
# 2. Repeat the string "Code" 7 times and print the result.
print("Code"*7)
# 3. Extract the substring "top" from the string "Octopocalypse".
print("Octopocalypse"[2:5])
# 4. Reverse the string "Python".
print("Python"[::-1])
# Print the results of each operation.

# Task 2: Advanced String Operations
# ----------------------------------
# Write a Python function that:
# 1. Counts the number of vowels in a given string.
# 2. Replaces all occurrences of a given character in a string with another character.

def count_vowels(s):
    # vowel_count = 0
    # vowel_count=vowel_count+s.count("a")
    # vowel_count=vowel_count+s.count("e")
    # vowel_count=vowel_count+s.count("i")
    # vowel_count=vowel_count+s.count("o")
    # vowel_count=vowel_count+s.count("u")
    # vowel_count=vowel_count+s.count("A")
    # vowel_count=vowel_count+s.count("E")
    # vowel_count=vowel_count+s.count("I")
    # vowel_count=vowel_count+s.count("O")
    # vowel_count=vowel_count+s.count("U")
    vowels="aeiouAEIOU"
    vowel_count=sum(1 for char in s if char in vowels)
    print(vowel_count)
    return(vowel_count)
    pass

def replace_char(s, old, new):
    return s.replace(old, new)
    pass

# Task 3: String Formatting
# -------------------------
# Write a Python function that accepts a user's first name and last name, then returns a string formatted as "Last, First".
# If the name is not provided (either first or last), it should default to "Unknown".

def format_name(first_name="Unknown", last_name="Unknown"):
    if(first_name==None or last_name==None):
        return "Unknown"
    else: return (f'{last_name}, {first_name}')
    pass

# Task 4: String Validation
# -------------------------
# Write a Python function that checks if a given string is a valid email address. For simplicity, assume an email is valid if it contains exactly one "@" symbol and at least one "." after the "@".

def is_valid_email(email):
    if email.find("@") != 1:
        return False
    # if I split on the last "." then the @ should be before that
    
    pass

