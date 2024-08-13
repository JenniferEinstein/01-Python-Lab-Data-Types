# mixed_operations.py

# Task 1: Combined Operations
# ---------------------------
# Evaluate the following complex expressions:
# 1. (3 + 5 * 2) > (10 / 2) and (not (4 == 4) or 7 % 2 == 1)
#       13>5 and false or true => true and false or true => true and true => true
import math


print(True)
# 2. "Data" * 3 + "Science" > "DataScience"
#       DataDataDataScience > DataSciene
#       both sides of the equation evaluate to True, so they are equal (NO, but why?)
print (False)

# 3. 100 > 50 and "Code" == "code".upper()
#       100 IS greater than 50 but Code isn't CODE
print(False)

# Write the answers in comments below each expression and print the results.

# Task 2: Type Conversion and Operations
# --------------------------------------
# Write a Python function that takes an integer and a string representing a number (e.g., "25") and:
# 1. Converts the string to an integer and adds it to the original integer.
# 2. Converts the sum back to a string and concatenates it with the original string.
# 3. Returns the final result.

def combine_and_convert(num, num_str):
    # converted = int(num_str)
    # added = num+converted
    # strung = str(added)
    # final = strung+num_str
    # print(final)

    strung = str(num+int(num_str))
    final = strung+num_str
    print(final)
    return final
    pass

# Task 3: Mixed Type Handling
# ---------------------------
# Write a Python function that takes two parameters, a number and a boolean, and:
# 1. Returns the number squared if the boolean is True.
# 2. Returns the square root of the number if the boolean is False.

def mixed_operations(num, flag):
    if flag == True:
        return num*num
    else:
        return math.sqrt(num)
    pass

# Task 4: Data Type Comparison
# ----------------------------
# Write a Python function that compares the data types of two inputs and returns True if they are the same, and False otherwise.

def compare_types(a, b):
    if type(a) == type(b):
        return True
    else:
        return False
    pass
