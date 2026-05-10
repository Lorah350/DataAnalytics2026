# loop_love.py
# This script demonstrates basic iteration in Python using a for-loop.
# It iterates through a list of descriptive words and prints a formatted message for each item.

# Define a list of adjectives that convey the meaning of "great".
# This list serves as the iterable for the loop.
great_words = ["amazing", "awesome", "excellent", "fantastic", "incredible"]

# Iterate through each element in the list.
# 'word' represents the current item during each loop cycle.
for word in great_words:
    # Use an f-string to embed the current word into the output string.
    print(f"Loops are {word}!")

# This statement executes after the loop completes all iterations.
# It provides a final message indicating the end of the process.
print("I <3 loops")
