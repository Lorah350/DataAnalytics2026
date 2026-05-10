# ranked_list.py
# This script demonstrates how to use enumerate() inside a for-loop to create
# a numbered list. It also shows how to add conditional logic to highlight
# the top-ranked item, and how to reverse the list while keeping numbering
# starting at 1.

# -----------------------------------------
# 1. Create a list of items (your choice)
# -----------------------------------------
# You can replace these with foods, cities, skills, pets, etc.
favorite_cities = ["Tokyo", "Cape Town", "Barcelona", "Seoul", "Vancouver"]

# -----------------------------------------
# 2. Print the list using enumerate()
# -----------------------------------------
# enumerate() gives us both the index (starting at 0 by default)
# and the item itself. We set start=1 so numbering begins at 1.
print("Ranked List (Normal Order):")
for index, city in enumerate(favorite_cities, start=1):

    # Build the base output string
    line = f"{index}. {city}"

    # If this is the first item (index == 1), mark it as the top pick
    if index == 1:
        line += " <- top pick!"

    print(line)

# -----------------------------------------
# 3. BONUS: Print the list in reverse order
# -----------------------------------------
# reversed() returns the list in reverse without modifying the original.
print("\nRanked List (Reversed Order):")
for index, city in enumerate(reversed(favorite_cities), start=1):
    print(f"{index}. {city}")
