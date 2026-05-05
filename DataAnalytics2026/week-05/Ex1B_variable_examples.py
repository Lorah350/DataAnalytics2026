# Customer information variables
customer_id = 102938        # assuming numeric ID assigned by system
customer_name = "Alicia Moyo"   # full name stored as one string
customer_gender = "Female"      # assuming gender stored as text
customer_dob = "1990-07-14"     # stored as string in YYYY-MM-DD format
drivers_license_number = "NC-4892034"   # string because it may contain letters
auto_policy_number = "POL-778920"       # string because policy numbers aren't pure numbers

# Notes about assumptions
# customer_id: assumed numeric, but could also be a string if IDs include letters
# customer_name: stored as one string, but could be split into first/last
# customer_gender: assumed text, but could be standardized codes (M/F/X)
# customer_dob: stored as string, but could be a date object
# drivers_license_number: must be string because states mix letters + numbers
# auto_policy_number: string because policy numbers often include letters

# Personal variables
my_name = "Lorah Mwembe"          # using full name as one string
my_birth_city = "Harare"           # city where I grew up
my_birth_state = "Zimbabwe"       # country/state equivalent


# -------------------------------
# EXERCISE 1B – RESERVED WORDS
# -------------------------------

# (a) Full list of Python reserved words:
# False, None, True,
# and, as, assert, break, class, continue,
# def, del, elif, else, except,
# finally, for, from, global,
# if, import, in, is, lambda,
# nonlocal, not, or, pass,
# raise, return, try, while, with, yield

# (b) Five keyword definitions:

# 1. lambda — Creates an anonymous function (a function with no name). Useful for short, one‑line functions.
#    Example: lambda x: x * 2

# 2. nonlocal — Used inside nested functions to modify a variable from the outer function’s scope.
#    This is different from ^^global^^ because it only affects the nearest outer function.

# 3. yield — Turns a function into a generator. Instead of returning once, it pauses and resumes,
#    producing a sequence of values over time.

# 4. assert — Used for debugging. It checks a condition and raises an error if the condition is False.

# 5. raise — Forces a specific error to occur. Often used in validation or error handling.
