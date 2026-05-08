#Formula = Radius = Diameter ÷ 2
#Area = π × r² (Circle area and radius)

#Diameter is the distance across the circle going through centre
#Using the day of my birthday as the diameter(14)
diameter =14

#Radius is half of the diameter, hence r=d/2
# math.pi gives me a precise value for π

import math   # using math.pi to get an accurate value for π

# My birthday is 11/14, so I'm using the 14 as the diameter
diameter = 14

# Radius is just half of the diameter
radius = diameter / 2

# Formula for area of a circle: π * r^2
area = math.pi * (radius ** 2)

#Display results
# Printing the result in the format the assignment wants
print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))
