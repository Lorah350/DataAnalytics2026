# Ex3A_string_cleaning.py
# Cleaning up messy contact data so it's actually usable

# Step 2: Here's the messy data my colleague sent me.
# The names have weird capitalization and the salaries have symbols.
name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"

salary_1 = "$82,500"
salary_2 = "$74,000"

# Step 3: First, let me convert all the names to lowercase.
# This helps standardize everything before I format it nicely.
print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

# Step 4: Now I'll convert the names to title case.
# This makes them look clean and professional.
print(name_1.title())
print(name_2.title())
print(name_3.title())

# Step 5: The salaries have a $ sign, which stops Python from treating them as numbers.
# I'll remove the $ so I can work with the values later.
clean_salary_1 = salary_1.replace("$", "")
clean_salary_2 = salary_2.replace("$", "")

print(clean_salary_1)
print(clean_salary_2)

# Let me check what type these values are now.
# Even though they look like numbers, they're still strings.
print(type(clean_salary_1))
print(type(clean_salary_2))

# Step 6: Now I want salary_1 as a real integer.
# I need to remove both the $ and the comma, then convert it to int.
salary_1_int = int(salary_1.replace("$", "").replace(",", ""))

print(salary_1_int, type(salary_1_int))
