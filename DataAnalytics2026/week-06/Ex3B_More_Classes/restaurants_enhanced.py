# restaurants_enhanced.py
# This is my enhanced Restaurant class with tracking for customers served and ratings.

class Restaurant:
    """A simple class to model a restaurant and track customers + ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        try:
            num = int(input("How many customers served today? "))
            if num < 0:
                print("Number cannot be negative. Try again.")
                return
            self.number_served += num
        except ValueError:
            print("Please enter a valid whole number.")

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        while True:
            rating = input("Rate your experience 1-5 (5 = excellent): ")

            # Validate input
            if rating.isdigit():
                rating = int(rating)
                if 1 <= rating <= 5:
                    self.customer_ratings.append(rating)
                    avg = sum(self.customer_ratings) / len(self.customer_ratings)
                    print(f"Your rating was {rating}. The average rating is {avg:.2f}")
                    break
                else:
                    print("Rating must be between 1 and 5.")
            else:
                print("Please enter a whole number between 1 and 5.")

# Create restaurant objects
rest1 = Restaurant("Mama's Kitchen", "Soul Food")
rest2 = Restaurant("Sushi Palace", "Japanese")
rest3 = Restaurant("Pizza World", "Italian")

# Test number served
rest1.print_num_served()
rest1.add_num_served()
rest1.add_num_served()
rest1.print_num_served()

# Test ratings
rest1.customer_rating()
rest1.customer_rating()
rest1.customer_rating()
