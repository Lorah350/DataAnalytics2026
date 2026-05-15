# Function 1: Display a mailing label
# This function prints an address label using the information I pass in.

def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
    print()  # blank line for spacing


# Function 2: Add any amount of numbers together
# I use *nums so the function can accept one number or many numbers.

def add_numbers(*nums):
    total = sum(nums)
    numbers_text = " + ".join(str(n) for n in nums)
    print(f"{numbers_text} = {total}")
    print()


# Function 3: Display a receipt and calculate change
# If the person underpays, I show the remaining balance.

def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

    print()  # spacing

    display_mailing_label("Lorah Mwembe", "123 Sunshine Lane", "Charlotte", "NC", "28202")
display_mailing_label("Ava Johnson", "45 River Park Drive", "Atlanta", "GA", "30303")

add_numbers(10)
add_numbers(5, 15)
add_numbers(2, 4, 6, 8, 10)

display_receipt(50, 60)
display_receipt(40, 40)
display_receipt(75, 50)

