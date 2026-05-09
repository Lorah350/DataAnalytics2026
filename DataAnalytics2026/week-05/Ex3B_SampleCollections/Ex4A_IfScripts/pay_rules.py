# This script calculates a person's gross pay based on:
# - their hourly pay rate
# - how many hours they worked this week
# If they work more than 40 hours, the extra hours are paid at "time and a half"
# (which just means 1.5 times their normal hourly rate).

pay_rate = 17.30        # you can change this to test different values
hours_worked = 45       # change this too when testing

# First, let's assume no overtime and calculate regular pay
regular_hours = min(hours_worked, 40)   # you can only have up to 40 regular hours
regular_pay = regular_hours * pay_rate

# Now figure out overtime hours (if any)
# If someone worked less than or equal to 40 hours, overtime_hours becomes 0
overtime_hours = max(hours_worked - 40, 0)

# Overtime pay is paid at 1.5x the normal rate
overtime_pay = overtime_hours * pay_rate * 1.5

# Total gross pay is just regular pay + overtime pay
gross_pay = regular_pay + overtime_pay

# Show the results in a clean, friendly way
print("Pay rate: $", pay_rate)
print("Hours worked:", hours_worked)
print("Regular pay: $", format(regular_pay, ".2f"))
print("Overtime pay: $", format(overtime_pay, ".2f"))
print("Gross pay: $", format(gross_pay, ".2f"))
