# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

def check_valid_num(list):
    # Prompt user to pick one of the categories and check if number is valid
    while True:
        user_category = input("\nWhich category would you like to pick?\nType corresponding number: ")
        try:
            user_category = int(user_category)

            if 1 <= user_category <= len(list):
                return user_category
            else:
                print(f"Please enter a number between 1 and {len(list)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Create a loop that only ends when user is done ordering
while True:

    # Print food categories with corresponding values
    category_list = [key for key in menu.keys()]
    for item in category_list:
        print(f"{category_list.index(item) + 1}. {item}")

# Prompt user to pick one of the categories and check if number is valid
    user_category = check_valid_num(category_list)

    # Now lets print the menu
    # Create header names
    headers = ["ITEM #", "ITEM", "Price"]

    for item, price in menu[category_list[user_category - 1]].items():
        print(f"Item: {item}   Price: {price}")

    still_ordering = input("\nAre you still ordering? Enter anything to continue or (N)o to end. ")
    if still_ordering.upper() == "Y":
        continue
    elif still_ordering.upper() == "N":
        print("By have a great time!\n")
        break