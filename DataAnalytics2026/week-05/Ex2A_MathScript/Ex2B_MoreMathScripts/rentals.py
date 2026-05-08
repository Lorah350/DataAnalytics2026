# Rentals
# To figure out how many vans are needed, divide the number of people by the number
# of seats per van and round up because you can't rent part of a van. Then calculate
# the total rental cost and the cost per person.

import math

# Ask how many people are going on the tour
people = int(input("Enter the number of people going on the tour: "))
#                                                                     * tested code using 8 people
#                                                                     *result - cost per person: $31.25
#                                                                     *vans needed : 1  
# Vans seat 15 passengers each
seats_per_van = 15

# Vans cost $250 each
van_cost = 250

# Number of vans needed (rounded up)
vans_needed = math.ceil(people / seats_per_van)

# Total rental cost
total_cost = vans_needed * van_cost

# Cost per person
cost_per_person = total_cost / people

# Show the results
print(f"Vans needed: {vans_needed}")
print(f"Total rental cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
