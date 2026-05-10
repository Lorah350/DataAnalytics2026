# greeting.py (updated version)
# Now includes a special message for late-night hours.

current_hour = 2   # change this number to test different times

# First check the late-night condition
if current_hour >= 23 or current_hour < 4:
    print("What are you doing up so late??")

# Before 10am → morning
elif current_hour < 10:
    print("Good morning!")

# 10am until 5pm → day
elif current_hour < 17:
    print("Good day!")

# 5pm or later → evening
else:
    print("Good evening!")
