# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

# Step 2: Define the variables
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Step 3: Perform transformations

# --- Casting as integers ---
# int_a = int(a)        # ERROR: ValueError (string contains spaces and decimal)
int_b = int(b)          # Works: '55' → 55
# int_c = int(c)        # ERROR: ValueError (string contains letters)
# int_d = int(d)        # ERROR: ValueError (string contains letters)

# --- Casting as floats ---
float_a = float(a)      # Works: " 101.1 " → 101.1
# float_b = float(b)    # Works: '55' → 55.0 (optional to include)
# float_c = float(c)    # ERROR: ValueError (letters in string)
# float_d = float(d)    # ERROR: ValueError (letters in string)

# --- Special case for variable a ---
int_float_a = int(float(a))   # Works: float(a)=101.1 → int(101.1)=101

# Step 4: Print values and types
print("a:", a, type(a))
print("b:", b, type(b))
print("c:", c, type(c))
print("d:", d, type(d))

print("float_a:", float_a, type(float_a))
print("int_b:", int_b, type(int_b))
print("int_float_a:", int_float_a, type(int_float_a))

# Step 5: Comments explaining results:
# a) int(a) fails because " 101.1 " contains a decimal → ValueError
# b) float(a) works because float() accepts decimals and spaces
# c) int(float(a)) works because float(a) becomes 101.1, then int() removes decimals
# d) int(c) and float(c) fail because "402 Stevens" contains letters
# e) int(d) and float(d) fail because "Number 5 " contains letters
