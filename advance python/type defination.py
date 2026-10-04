# we can define typr of a varryable so we can use their properties and east to understand

a :  str = "ajay"
b : int = 23


def sum(a:int, b:int) -> int: # this outer int is showing about the return
    return a+b

sum(2,3)


# TYPING MODULE EXAMPLE
# -----------------------------------
# The typing module is used to give type hints in Python.

# Type hints help:
                   # 1. Improve code readability
                   # 2. Detect errors early
                   # 3. Help IDEs with suggestions/autocomplete

from typing import List  # same for tuoplr, dictionary , union etc.

# Function that accepts a list of integers and returns an integer

def find_total(numbers: List[int]) -> int:
    # numbers should be a list of integers
    # return value should be an integer

    total = sum(numbers)
    return total


# Calling the function
data = [10, 20, 30]

result = find_total(data)

print("Total:", result)