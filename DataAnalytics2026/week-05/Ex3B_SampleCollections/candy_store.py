# candy_store.py
# I'm putting together some fun candy + fruit flavor combinations.
# The goal is just to practice tuples, sets, and indexing in a way that feels simple.

# Step 2: First, I'm creating two tuples.
# Tuples are perfect here because these items don't need to change.
candy_types = ("Gummy Bears", "Lollipops", "Hard Candy")
flavors = ("Strawberry", "Mango", "Blue Raspberry")

# Step 3: Now I want to mix these together.
# I'll store the combinations in a set because I don't care about order,
# and sets automatically avoid duplicates.
candy_combos = set()

# I'm using the index positions to pair each candy with a flavor.
# This is just me being playful with the combinations.
candy_combos.add(candy_types[0] + " - " + flavors[1])
candy_combos.add(candy_types[1] + " - " + flavors[0])
candy_combos.add(candy_types[2] + " - " + flavors[2])

# Step 4: Time to show the results.
print("Today's candy options include:")
print(candy_combos)

# Step 5: I'm printing the set a few times to see what happens.
# Sets don't keep a fixed order, so the items may show up differently each time.
print(candy_combos)
print(candy_combos)
