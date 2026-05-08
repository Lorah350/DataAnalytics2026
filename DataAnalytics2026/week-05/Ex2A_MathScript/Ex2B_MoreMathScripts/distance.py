# Distanceis the leghth of a straight line between two coordinate points 
# It is calculated using the distance formula derived from the
# Pythagorean Theorem

import math

# Input the two points
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Apply the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result formatted to two decimal places
print(f"Distance between the points: {distance:.2f}")#


