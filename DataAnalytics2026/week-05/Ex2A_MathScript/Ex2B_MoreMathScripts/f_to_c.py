# Temperature conversion is really just adjusting for how the two scales measure heat.
# Fahrenheit starts at a different “zero” than Celsius, so we:
# 1. Remove the extra 32 degrees
# 2. Shrink the number because Celsius degrees are bigger

# Formula: C = (F - 32) * 5/9

#Temperature conversion from Fahrenheit to Celsius using  (72°F)

# Use 72 as the Fahrenheit temperature
fahrenheit = 72

# Convert Fahrenheit to Celsius using the formula C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * (5/9)

# Display the result
print(f"{fahrenheit} F is equal to {celsius:.2f} C.")

 


