# Rule of 72 is a shortcut used to estimate how long money takes to double
# You divide 72 by the interest rate (in percent) to get the time in years
# Example: if the interest rate is 5%, then 72 / 5 = 14.4 years

# My current savings (using an example amount)
current_savings = 5000   # I'm pretending I have $5,000 saved

# The interest rate I expect (using an example percent)
interest_rate = 5        # I'm using 5% interest for this example

# Use the Rule of 72 to estimate how many years it will take to double
# This is a quick estimate, not an exact calculation
years_to_double = 72 / interest_rate

# Calculate what the doubled amount would be
doubled_balance = current_savings * 2

# Display the results in a clean, readable way
print("My current savings is " + format(current_savings, ".2f") + ".")
print("At a " + format(interest_rate / 100, ".0%") + " interest rate, my savings account will be")
print("worth " + format(doubled_balance, ".2f") + " in " + format(years_to_double, ".1f") + " years")
