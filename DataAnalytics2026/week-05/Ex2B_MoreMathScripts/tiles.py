# Tiles need:
# To figure out how many boxes of tiles are needed, start by finding the room's area
# in square feet. Each tile covers one square foot, and each box holds twelve tiles.
# Since stores don't sell partial boxes, the number has to be rounded up.
# I also want to buy  10% extra to cover mistakes or broken tiles.

import math

# Collect room dimensions
length = float(input("Enter the room length in feet: "))
width = float(input("Enter the room width in feet: "))

# Calculate total tiles needed based on the room area
area = length * width

# Each box contains 12 tiles
tiles_per_box = 12

# Boxes needed for the exact area (rounded up)
boxes_needed = math.ceil(area / tiles_per_box)

# Add 10% extra tiles for safety
extra_tiles = area * 0.10
total_tiles_with_extra = area + extra_tiles

# Total boxes including the extra tiles (rounded up)
total_boxes = math.ceil(total_tiles_with_extra / tiles_per_box)

# Show the results
print(f"Boxes needed (no extra): {boxes_needed}")
print(f"Total boxes with 10% extra: {total_boxes}")
