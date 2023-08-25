"""

Purpose: Perform basic arithmetic.

Author: Matt Riley

This script illustrates getting input from the user and using basic methods.

When we install Python, it comes with the Python standard library.
Nearly all scripts will import at least one module from the standard library.

We can install additional, third-party modules using pip.
We'll do that later. 

All scripts in this repository use only the standard library.

@uses math module for pi constant

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------

# get the numbers from the user - input result is always a string
# Use \n to add a blank new line to the terminal before we ask for input
string1 = input("\nPlease enter number 1: ")
string2 = input("Please enter number 2: ")
string3 = input("Please enter number 3: ")

# convert the input strings to numbers
int1 = int(string1)
int2 = int(string2)
int3 = int(string3)
nums = (int1, int2, int3)

print()

# log the results
logger.info(f"The sum of {int1}, {int2}, and {int3} is {sum(nums)}.")
logger.info(f"The average of {int1}, {int2}, and {int3} is {round(sum(nums) / len(nums), 2)}.")
logger.info(f"The product of {int1}, {int2}, and {int3} is {int1 * int2 * int3}.")
logger.info(f"The minimum of {int1}, {int2}, and {int3} is {min(nums)}.")
logger.info(f"The maximum of {int1}, {int2}, and {int3} is {max(nums)}.")
