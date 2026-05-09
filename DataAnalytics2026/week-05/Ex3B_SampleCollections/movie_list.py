# movie_list.py
# I'm creating a simple list of movies and practicing how to work with collections.

# Step 2: Here's my starting list of movies.
# I picked a few I like, and I made sure they're not already in alphabetical order.
movies = ["Inception", "The Woman King", "Avatar"]

# Step 3: I want to describe my list using len(), which tells me how many items are inside.
print(f"The list movies includes my top {len(movies)} favorite movies.")
print(movies)   # Just showing the whole list as it is.

# Step 4a: Using sorted() gives me a *temporary* alphabetical version of the list.
print(sorted(movies))   # This shows the sorted version...
print(movies)           # ...but the original list stays the same.

# Step 4b: Now I'm sorting the list *permanently* using .sort().
movies.sort()
print(movies)   # Now the list itself is changed.

# Step 5: Adding one more movie using .append().
movies.append("Black Panther")
print(f"Updated list now includes {len(movies)} movies.")
print(movies)
