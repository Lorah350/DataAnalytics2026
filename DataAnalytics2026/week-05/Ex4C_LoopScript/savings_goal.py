# savings_goal.py
# This script models how your savings grow week by week until you reach a financial goal.
# It uses a while loop because we don't know ahead of time how many weeks it will take.
# The loop continues running until the balance reaches or exceeds the goal.

# -----------------------------
# 1. Define starting variables
# -----------------------------

# Your starting amount of money in the bank.
starting_balance = 500.00

# The total amount you want to save.
savings_goal = 2000.00

# How much you plan to save every week.
weekly_savings = 150.00

# We track the current balance separately so we don't overwrite the original starting value.
current_balance = starting_balance

# -----------------------------
# 2. While loop to grow savings
# -----------------------------
# The loop runs as long as the current balance is still below the goal.
while current_balance < savings_goal:

    # Add this week's savings to the balance.
    # This is the core action that moves us toward the goal.
    current_balance += weekly_savings

    # Check if the balance has passed 50% of the goal but is still below 75%.
    # This helps us give more specific feedback as we get closer.
    if 0.50 * savings_goal <= current_balance < 0.75 * savings_goal:
        print(f"Almost there! This week my balance is up to {current_balance:.2f}.")

    # Check if the balance has reached at least 75% of the goal.
    # At this point, we simulate buying a small treat.
    elif current_balance >= 0.75 * savings_goal and current_balance < savings_goal:
        treat_cost = 10.00  # A small reward for staying consistent.
        current_balance -= treat_cost  # Subtract the treat cost from the balance.
        print(f"So close! After treating myself, my balance is up to {current_balance:.2f}.")

    # If we are still early in the savings journey, use the standard message.
    else:
        print(f"This week my balance increased to {current_balance:.2f}.")

# -----------------------------
# 3. Final message after loop
# -----------------------------
# Once the loop ends, we know the goal has been reached.
print(f"Goal met! My current balance is {current_balance:.2f}.")
