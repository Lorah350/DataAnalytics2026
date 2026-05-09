# A year is a leap year in the Gregorian calendar if:
# 1. It is divisible by 4
# BUT
# 2. If it's divisible by 100, it's NOT a leap year
# UNLESS
# 3. It's also divisible by 400 — then it IS a leap year again
#
# This weird rule exists to keep the calendar aligned with Earth's orbit.

year = 2000   # change this to test different years

if (year % 400 == 0):
    print(year, "is a leap year (divisible by 400).")
elif (year % 100 == 0):
    print(year, "is NOT a leap year (divisible by 100 but not 400).")
elif (year % 4 == 0):
    print(year, "is a leap year (divisible by 4).")
else:
    print(year, "is NOT a leap year (not divisible by 4).")
