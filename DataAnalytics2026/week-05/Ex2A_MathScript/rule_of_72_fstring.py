# Rule of 72 is a shortcut used to estimate how long money takes to double.
# You divide 72 by the interest rate (in percent) to get the time in years.

# Ask the user for their current savings
current_savings = float(input("What is your current savings amount? "))
current_savings = 50000

# Ask the user for the interest rate they expect (as a percent)
interest_rate = float(input("What is the interest rate (in %)? "))
interest_rate = 5

# Use the Rule of 72 to estimate how many years it will take to double
years_to_double = 72 / interest_rate

# Calculate the doubled amount
doubled_balance = current_savings * 2

# Display the results using f-strings (cleaner and easier to read)
print(f"Your current savings is {current_savings:.2f}.")
print(f"At a {interest_rate:.0f}% interest rate, your savings account will be")
print(f"worth {doubled_balance:.2f} in about {years_to_double:.1f} years.")

# Pitfalls of using input():
# - input() always gives you a string, so you MUST convert it using float() to do math.
# - If the user types letters instead of numbers, the program will crash.
# - If the user types '5%' instead of just 5, float() will fail.
# - If the user enters 0 for the interest rate, the program will crash (division by zero).
# - If the user presses Enter without typing anything, the script will error out.
# - Users can accidentally add spaces or symbols that break the conversion.
