# Task 1: Complex Boolean Expressions
# -----------------------------------
# Evaluate the following boolean expressions:
# 1. (10 > 5) and (5 <= 3) or (100 == 100)
        # True and False or True
print(True)

# 2. not (7 != 7) or ((3 < 2) and (4 == 4))
        # True or False and True
print(True)
# 3. (4 ** 2 > 15) and ((100 / 10) < 9) or (5 == 5 and not (10 == 10))
        # True and True or True and False
print(True)

# Write the answers in comments below each expression and print the results.

# Task 2: Boolean Function
# ------------------------
# Write a Python function that takes two numbers as input and returns True if the first number is divisible by the second, and False otherwise.

def is_divisible(x, y):
    if x % y == 0:
        return True
    else: 
        return False

    pass

# Task 3: Complex Logical Operations
# ----------------------------------
# Write a Python function that evaluates whether a given integer is:
# 1. Positive, even, and divisible by 3.
# 2. Negative, odd, and greater than -10.

def complex_check(n):
    if (n>0 and n%2==0 and n%3==0) or (n<0 and n%2==1 and n>-10):
        return True
    pass

# Task 4: Boolean Type Conversion
# -------------------------------
# Convert the following expressions to booleans using the `bool()` function and explain the results:
# 1. 0
# 2. 3.14
# 3. -100
# 4. ""
# 5. "False"
# 6. []

# Use the `bool()` function and print the results with comments explaining the outcomes.

print(bool(0))
    # 0 is a falsy value
print(bool(3.14))
    # fractions have a truthy value
print(bool(-100))
    # integers have a truthy value 
print(bool(""))
    # Empty objects, including strings, are always False
print(bool("False"))
    # A string with anything in it -- even the word False -- is a truthy value. 
print(bool([]))
    # Empty objects are always False



