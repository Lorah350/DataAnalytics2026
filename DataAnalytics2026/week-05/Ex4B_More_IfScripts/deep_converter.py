# This script takes a department code (a number)
# and prints the matching department name.
# Using if/elif/else logic — simple, straightforward.

dept_code = 12   # change this number to test different codes

if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
elif dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")
else:
    # This catches any code that isn't in the list
    print("Unknown department code:", dept_code)

    # Same idea as the first script, but using match/case.
# This is Python's newer, cleaner way to handle multiple exact matches.

dept_code = 12   # change this number to test different codes

match dept_code:
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        # The underscore means "anything else"
        print("Unknown department code:", dept_code)

