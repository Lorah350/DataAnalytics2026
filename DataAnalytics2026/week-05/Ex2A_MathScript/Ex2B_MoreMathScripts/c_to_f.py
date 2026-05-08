#This is the opposite of f_to_c.py
#Instead of shrinking the number we stretch it


# Why? because celcius are bigger
#(Celcius number is multiplied by 9 divided 5 plus 32)
#Fareinheit starts 32 degrees higher

# # Temperature conversion from Celsius to Fahrenheit using  (22°C)

# Use 22 as the Celsius temperature
celsius = float(22)

# Convert Celsius to Fahrenheit using the formula F = C * 9/5 + 32
fahrenheit = (celsius * 9/5) + 32

# Display the result
print(f"{celsius} C is equal to {fahrenheit:.2f} F.")

