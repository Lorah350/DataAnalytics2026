# Global customer list (created once at the top of the script)
cust_list = []

class RewardsProgram:
    """A simple class to store customer info for a restaurant rewards program."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        # Add customer info as a tuple to the global list
        cust_list.append((self.cust_name, self.phone, self.email))


# Creating three customers
cust1 = RewardsProgram("Lorah Mwembe", "704-555-1111", "lorah@example.com")
cust2 = RewardsProgram("Ava Johnson", "980-555-2222", "ava@example.com")
cust3 = RewardsProgram("Marcus Lee", "336-555-3333", "marcus@example.com")

# Running methods for each customer
cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()

cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()

cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

# Print the full customer list
print("\nCustomer List:")
print(cust_list)
