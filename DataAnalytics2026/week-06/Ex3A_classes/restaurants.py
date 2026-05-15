# This class represents a restaurant and the type of food it serves.
class Restaurant:
    """A simple class to store a restaurant's name and the type of food it serves."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


# Creating three restaurant objects
rest1 = Restaurant("Mama's Kitchen", "soul food")
rest2 = Restaurant("Sakura House", "Japanese cuisine")
rest3 = Restaurant("Bella Pasta", "Italian food")

# Calling the methods for each restaurant
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()
