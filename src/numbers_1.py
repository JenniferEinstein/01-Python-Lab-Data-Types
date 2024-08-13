# Task 1: Complex Arithmetic
# ---------------------------
# Evaluate the following expressions and assign the results to variables:
# 1. (25 + 30) * (15 / 3) - 4 ** 2
        #       259.0
first = (25 + 30) * (15 / 3) - 4 ** 2
print(first)
# 2. ((45 % 6) * 2) + (100 / 5) ** 3
        #       8006.0
second = ((45 % 6) * 2) + (100 / 5) ** 3
print(second)
# 3. (50 * 2) - ((3 ** 2) * (8 + 5)) / (4 % 3)
        #       -17.0
third = (50 * 2) - ((3 ** 2) * (8 + 5)) / (4 % 3)
print(third)

# Write the answers in comments below each expression and print the results.

# Task 2: Type Identification
# ---------------------------
# Identify the data type of the following expressions:
# 1. 10 + 5.0
        # float
print("float")
# 2. 100 / 3
        # float
print("float")
# 3. 100 // 3
        # integer
print("integer")
# 4. 4 ** 0.5
        # float
print("float")

# Use the `type()` function to verify the data types and print them.
print(type(10 + 5.0))
print(type(100 / 3))
print(type(100 // 3))
print(type(4 ** 0.5))

# Task 3: Arithmetic Error Handling
# ---------------------------------
# Write a Python function that attempts to divide two numbers and catches any potential errors (e.g., division by zero).
# Return a custom error message if an error occurs.

def safe_divide(a, b):
    # Your code here
    if b==0:
        return "Error: Division by zero"
    elif(not a or not b):
        return "One or more of your numbers doesn't exist"
    elif type(a)==str or type(b)==str:
        return "No strings allowed"
    else: return a/b
    pass

# Task 4: Advanced Arithmetic
# ---------------------------
# Write a Python function that takes an integer and returns:
# 1. The factorial of the number.
# 2. The sum of all digits in the number.

def factorial(n):
    # return 1 if
    pass

def sum_of_digits(n):
    # Your code here
    pass

