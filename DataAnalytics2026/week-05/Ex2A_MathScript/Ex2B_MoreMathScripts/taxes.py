#What are taxes?
# Taxes are a percentage of your income that you must pay to the government.
# This script calculates how much tax is owed based on a fixed income amount.

# Use 55000 as the income amount
income = float(55000)

# Use a 25% tax rate
tax_rate = 0.23

# Calculate the tax owed
tax_owed = income * tax_rate

# Display the result(two decimal places)
print(f"On an income of ${income:.2f}, the tax owed is ${tax_owed:.2f}.")
