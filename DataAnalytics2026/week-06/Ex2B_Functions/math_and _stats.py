import random      # pulling random numbers and samples
import math        # using pi and rounding functions
import statistics  # doing averages, medians, modes, etc.

# Setting up my starting values
vals_1_100 = range(1, 100)                     # numbers from 1 to 99
vals_sample = random.sample(vals_1_100, 75)    # 75 unique random values
vals_choices = random.choices(vals_1_100, k=200)  # 200 random values (duplicates allowed)
radius = random.randint(3, 10)                 # random radius for the circle
pi = math.pi                                   # using pi from math module

# Working with the 75-value sample
sample_sum = sum(vals_sample)                  # total of the 75 numbers
sample_avg = statistics.mean(vals_sample)      # average of the sample
sample_median = statistics.median(vals_sample) # middle value of the sample

# Working with the 200-value superset
choices_avg = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_stdev = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# Modeling the circle using the formula area = π * r^2
area = pi * (radius ** 2)
area_up = math.ceil(area)                      # rounding the area up
area_down = math.floor(area)                   # rounding the area down

# Printing everything in the format the lab wants
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_median}")

print('\n')  # blank line

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_avg}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

print('\n')  # blank line

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_down} (rounded down to the nearest integer)")
