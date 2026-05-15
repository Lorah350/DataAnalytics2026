# Lambda that doubles whatever value is passed in
doubler = lambda n: n * 2

# Testing the doubler
print(doubler(8))
print(doubler(-4))
print(doubler("banana"))   # repeats the string twice


# Lambda that triples whatever value is passed in
tripler = lambda n: n * 3

# Testing the tripler
print(tripler(8))
print(tripler(-4))
print(tripler("banana"))   # repeats the string three times


# Function that returns a lambda multiplier
# This saves me from writing the same lambda over and over
def multiplier(num):
    return lambda n: n * num


# Creating multipliers from 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Testing each multiplier
print(quadrupler(3))
print(quintupler(3))
print(sextupler(3))
print(septupler(3))
print(octupler(3))
print(nonupler(3))
print(decupler(3))
