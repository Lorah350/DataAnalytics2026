# sales_performance.py
# This script processes a list of monthly sales records.
# Each record is stored as a tuple containing:
# (salesperson_name, region, total_sales)
# The goal is to unpack each tuple directly in the loop, print a formatted summary,
# identify top performers, and optionally calculate total sales across all employees.

# -----------------------------------------
# 1. Sales data provided in the assignment
# -----------------------------------------
sales_data = [
    ('Marcus Webb', 'East', 4250.00),
    ('Priya Sharma', 'West', 5875.50),
    ('DeShawn Carter', 'East', 3100.75),
    ('LaTonya Rivers', 'South', 6420.00),
    ('Bob Nguyen', 'West', 4980.25),
]

# -----------------------------------------
# 2. BONUS: Track total sales across all reps
# -----------------------------------------
total_sales = 0  # This will accumulate the sum of all sales amounts.

# -----------------------------------------
# 3. Loop through each record and unpack tuple
# -----------------------------------------
for name, region, amount in sales_data:
    # Print the formatted summary line for each salesperson.
    # Using comma formatting for readability (e.g., $4,250.00).
    print(f"{name} ({region}): ${amount:,.2f}")

    # Add this salesperson's sales to the running total.
    total_sales += amount

    # Conditional check for top performers.
    # If their sales exceed $5,000, print an additional line.
    if amount > 5000:
        print("  ^ Top performer!")

# -----------------------------------------
# 4. BONUS: Print total sales after the loop
# -----------------------------------------
print(f"\nOverall Total Sales: ${total_sales:,.2f}")
