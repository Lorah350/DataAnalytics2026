# address_entry.py
# I'm building a dictionary to store someone's contact information,
# and then formatting it so it looks like a real mailing address.

# Step 1: Here's my starting dictionary.
# Each key describes what the value represents.
contact_info = {
    "name": "Lorah Mwembe",
    "address": "123 Main Street",
    "city": "Charlotte",
    "state": "NC",
    "zip": "28277"
}

# Step 2: Printing the address in a clean, mailing-style format.
# I'm using a multi-line f-string so it prints like a real label.
print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

# Step 3: Now I'm removing the name key from the dictionary.
# Maybe I want to store the name in a more detailed way.
contact_info.pop("name")

# Step 4: Creating a new dictionary for the full name.
# This lets me break the name into first and last.
full_name = {
    "first name": "Lorah",
    "last name": "Mwembe"
}

# Step 5: Adding an honorific (like Ms., Mr., Dr., etc.)
# I'm using update() because it's the cleanest way to add a new key:value pair.
full_name.update({"honorific": "Ms."})

# Step 6: Adding the full_name dictionary into contact_info.
# Now contact_info contains another dictionary inside it.
contact_info.update({"full_name": full_name})

# Step 7: Printing the address again, now using the updated structure.
# I need to pull the name pieces from the nested dictionary.
print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")
