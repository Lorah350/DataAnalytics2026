# min_max.py
# This script finds the smallest and largest of three numbers
# using only if/else logic — no built-in min() or max() allowed.

# Assign values to a, b, and c (change these to test different cases)
a = 12
b = 7
c = 19

# -----------------------------
# FINDING THE SMALLEST NUMBER
# -----------------------------
# Start by assuming a is the smallest
smallest = a

# If b is smaller than what we currently think is the smallest, update it
if b < smallest:
    smallest = b

# Same check for c
if c < smallest:
    smallest = c

# -----------------------------
# FINDING THE LARGEST NUMBER
# -----------------------------
# Start by assuming a is the largest
largest = a

# If b is bigger than what we currently think is the largest, update it
if b > largest:
    largest = b

# Same check for c
if c > largest:
    largest = c

# -----------------------------
# DISPLAY RESULTS
# -----------------------------
print("The smallest number is:", smallest)
print("The largest number is:", largest)
