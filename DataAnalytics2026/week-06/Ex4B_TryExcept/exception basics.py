# -----------------------------------------
# ValueError
# -----------------------------------------
print("\n--- ValueError Example 1 ---")
try:
    num = int("banana")   # girl… this is not a number
except ValueError:
    print("ValueError: Yeah… Python said 'be serious'. Can't turn that into an int.")
else:
    print(num)
finally:
    print("Let's try another one...")

print("\n--- ValueError Example 2 ---")
try:
    float("hello")        # also not a number, besty
except ValueError:
    print("ValueError: Nope. That string is not floating anywhere.")
else:
    print("Conversion worked:", result)
finally:
    print("Let's try another one...")


# -----------------------------------------
# NameError
# -----------------------------------------
print("\n--- NameError Example 1 ---")
try:
    m = banana   # banana is not defined, just vibes
except NameError:
    print("NameError: Besty… you tried to use a variable that doesn’t exist.")
else:
    print(m)
finally:
    print("Let's try another one...")

print("\n--- NameError Example 2 ---")
try:
    print(x)     # x said “who me?”
except NameError:
    print("NameError: Python said 'I don’t know that man'.")
else:
    print(x)
finally:
    print("Let's try another one...")


# -----------------------------------------
# TypeError
# -----------------------------------------
print("\n--- TypeError Example 1 ---")
try:
    result = "hello" + 5   # mixing vibes and numbers
except TypeError:
    print("TypeError: You can’t add a string and an int, besty. Python refuses.")
else:
    print(result)
finally:
    print("Let's try another one...")

print("\n--- TypeError Example 2 ---")
try:
    len(42)   # 42 has no length, just confidence
except TypeError:
    print("TypeError: len() said 'I only work on things you can count through'.")
else:
    print("Length:", length)
finally:
    print("Let's try another one...")


# -----------------------------------------
# SyntaxError
# -----------------------------------------
# NOTE: SyntaxError can't happen in running code unless we eval/exec it.

print("\n--- SyntaxError Example 1 ---")
try:
    eval("5 +")   # unfinished business
except SyntaxError:
    print("SyntaxError: This expression is giving 'half-baked'.")
else:
    print("Expression evaluated successfully.")
finally:
    print("Let's try another one...")

print("\n--- SyntaxError Example 2 ---")
try:
    exec("if True print('hi')")   # missing colon, chaos
except SyntaxError:
    print("SyntaxError: Python said 'put that colon back immediately'.")
else:
    print("Exec ran successfully.")
finally:
    print("Let's try another one...")
