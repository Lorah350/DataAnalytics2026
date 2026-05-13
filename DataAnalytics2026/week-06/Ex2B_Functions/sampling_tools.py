import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# a) Product of the Day
product_of_the_day = random.choice(products)
print("Product of the Day:", product_of_the_day)

# b) Usability survey items (3 unique products)
survey_items = random.sample(products, 3)
print("Usability Survey Items:", survey_items)

# c) Shuffled product list
random.shuffle(products)
print("Shuffled Products:", products)

# d) Simulated daily transaction count
transactions = random.randint(50, 300)
print("Daily Transaction Count:", transactions)




