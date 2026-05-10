# Starting values — nothing fancy, just two numbers to play with
x = 100
y = 20

# a) First check: does x divided by y equal 5?
# I'm basically asking: "If I split 100 into groups of 20, do I get 5?"
if x / y == 5:
    print("x divided by y is 5")
    # Since the condition was true, the instructions say to reset x to 1
    x = 1
else:
    # If something went wrong, this message helps us notice it
    print("are the variables set up correctly?")

# b) Now x has changed, so we check again with the new value.
# Does x times y equal y? With x = 1, this becomes 1 * 20 == 20.
if x * y == y:
    print("now x times y is y")
    # The instructions say to update x again
    x = 10
else:
    # If the math doesn't match, we show what x actually is
    print("Whoops, x equals", x)

# c) Next check: is x less than y?
# With x = 10 and y = 20, this is true.
if x < y:
    print("x is less than y")
    # Doubling x because the condition was true
    x = x * 2
else:
    print("uh oh, x is not less than y")

# d) Now we check the opposite: is x greater than y?
# After doubling, x is now 20 — so it's NOT greater than y.
if x > y:
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

# e) Final summary — just showing where everything ended up
print(f"The final value of x is {x} and the final value of y is {y}")
