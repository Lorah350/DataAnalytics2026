# complex_taxes.py
# This script estimates weekly and annual gross pay,
# then applies a federal tax rate based on filing status
# and annual income. The goal is to calculate weekly tax withholding
# and net pay in a way that feels realistic but still simple.

# -----------------------------
# 1. STARTING VALUES (change these to test)
# -----------------------------
pay_rate = 20.00          # dollars per hour
hours_worked = 45         # hours this week
filing_status = "single"  # "single" or "joint"

# -----------------------------
# 2. WEEKLY GROSS PAY (copied from pay_rules.py logic)
# -----------------------------

# Regular hours are capped at 40
regular_hours = min(hours_worked, 40)
regular_pay = regular_hours * pay_rate

# Overtime is anything above 40 hours
overtime_hours = max(hours_worked - 40, 0)
overtime_pay = overtime_hours * pay_rate * 1.5

# Total weekly gross pay
weekly_gross = regular_pay + overtime_pay

# -----------------------------
# 3. ESTIMATE ANNUAL GROSS PAY
# -----------------------------
# There are 52 weeks in a year
annual_gross = weekly_gross * 52

# -----------------------------
# 4. DETERMINE TAX RATE
# -----------------------------
# Tax tables from the workbook:

# SINGLE FILER TAX TABLE
# Income Range            Tax Rate
# up to 44,725            12%
# 44,726 – 95,375         22%
# 95,376 – 182,100        24%
# 182,101 – 231,250       32%
# 231,251 – 578,125       35%
# 578,126 or more         37%

# JOINT FILER TAX TABLE
# up to 89,450            12%
# 89,451 – 190,750        22%
# 190,751 – 364,200       24%
# 364,201 – 462,500       32%
# 462,501 – 693,750       35%
# 693,751 or more         37%

# We'll use if/elif logic to assign the correct tax rate.

if filing_status == "single":
    if annual_gross <= 44725:
        tax_rate = 0.12
    elif annual_gross <= 95375:
        tax_rate = 0.22
    elif annual_gross <= 182100:
        tax_rate = 0.24
    elif annual_gross <= 231250:
        tax_rate = 0.32
    elif annual_gross <= 578125:
        tax_rate = 0.35
    else:
        tax_rate = 0.37

elif filing_status == "joint":
    if annual_gross <= 89450:
        tax_rate = 0.12
    elif annual_gross <= 190750:
        tax_rate = 0.22
    elif annual_gross <= 364200:
        tax_rate = 0.24
    elif annual_gross <= 462500:
        tax_rate = 0.32
    elif annual_gross <= 693750:
        tax_rate = 0.35
    else:
        tax_rate = 0.37

else:
    # If someone types something wrong
    print("Invalid filing status. Please use 'single' or 'joint'.")
    tax_rate = 0

# -----------------------------
# 5. WEEKLY TAX WITHHOLDING
# -----------------------------
weekly_tax = weekly_gross * tax_rate

# -----------------------------
# 6. NET PAY
# -----------------------------
net_pay = weekly_gross - weekly_tax

# -----------------------------
# 7. PRINT RESULTS (instructor‑style output)
# -----------------------------
print(f"You worked {hours_worked} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross:.2f}.")
print(f"Your filing status is {filing_status}.")
print(f"Your estimated annual gross income is ${annual_gross:,.2f}.")
print(f"Your tax withholding for the week is ${weekly_tax:.2f}.")
print(f"Your net pay is ${net_pay:.2f}.")
