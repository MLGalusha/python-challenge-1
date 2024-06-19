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

# This function will ask the user to pick a number from a list. It keeps asking until the user enters a valid number.
def check_valid_num(list, question):
    while True:
        # Ask the user the question provided and get their input
        user_choice = input(question)
        try:
            # Try to convert the input to an integer
            user_choice = int(user_choice)
            # Check if the number is within the valid range
            if 1 <= user_choice <= len(list):
                return user_choice
            else:
                # Tell the user if their number is out of range
                print(f"Please enter a number between 1 and {len(list)}.\n")
        except ValueError:
            # Tell the user if they didn't enter a valid number
            print("Invalid input. Please enter a valid number.\n")

# These are some constants we use to format our output nicely
header = f"{'ITEM #':<6} | {'ITEM':<23} | {'PRICE':<10}"
divider = "-" * len(header)

# This list will store the user's order
order_list = []
# This will keep track of the total price of the order
total_price = 0

print("Welcome to the variety food truck.")

# This loop will keep running until the user decides to stop ordering
while True:
    # Get a list of the category names from the menu dictionary
    category_list = [key for key in menu.keys()]
    # Print out the category options for the user to choose from
    for idx, item in enumerate(category_list, start=1):
        print(f"{idx}. {item}")

    # Ask the user to pick a category and make sure they pick a valid one
    cat_question = "Which category would you like to pick? "
    user_category = check_valid_num(category_list, cat_question)

    # Print out a nice header and divider for the item list
    print(f"{divider}\n{header}\n{divider}")
    i = 1
    item_list = []
    # Go through each item in the selected category
    for item, price in menu[category_list[user_category - 1]].items():
        if isinstance(price, dict):
            # If the item has sub-items (like different types of pizza), go through each sub-item
            for item_sub, price_sub in price.items():
                # Add each sub-item to the item list and print it out
                item_list.append({f"{item} - {item_sub}": price_sub})
                print(f"{i:<6} | {f'{item} - {item_sub}':<23} | {price_sub:<10}")
                i += 1
        else:
            # Add regular items to the item list and print them out
            item_list.append({item: price})
            print(f"{i:<6} | {item:<23} | {price:<10}")
            i += 1
    print(divider)

    # Ask the user to pick an item and make sure they pick a valid one
    item_question = "Which item would you like to order?  "
    item_num = check_valid_num(item_list, item_question)

    while True:
        # Get the dictionary for the selected item
        the_item = item_list[item_num - 1]
        # Get the key (item name) from the dictionary
        the_key = list(the_item.keys())[0]
        # Ask the user how many they want to order
        quantity = input(f"How many {the_key}s would you like to order? ")
        if quantity.isdigit() and int(quantity) >= 1:
            # Convert the quantity to an integer if it's valid
            quantity = int(quantity)
            break
        else:
            # Tell the user if they didn't enter a valid quantity
            print("Invalid input. Please type a valid number.\n")

    # Get the item name and price from the dictionary.
    # next(iter(...)) gets the first (and only) item from the dictionary.
    tkey, tprice = next(iter(the_item.items()))
    # Create a dictionary with the item, its price, and the quantity ordered
    temp_dict = {tkey: [tprice, quantity]}
    # Add the item's total price to the total order price
    total_price += tprice * quantity
    # Add the item to the order list
    order_list.append(temp_dict)

    # Ask the user if they want to continue ordering or not
    still_ordering = input("\nAre you still ordering? (N)o or enter anything else to continue ordering: ").lower()
    match still_ordering:
        case 'n':
            # Print out the receipt header and divider
            receipt_header = f"{'ITEM':<23} | {'PRICE':<10} | {'QUANTITY':<10}"
            receipt_divider = "-" * len(receipt_header)
            print(receipt_divider)
            print(f"{'RECEIPT':^46}")
            print(receipt_divider)
            print(receipt_header)
            print(receipt_divider)

            # Go through the order list and print each item with its price and quantity
            for item in order_list:
                temp_item_key = list(item.keys())[0]
                temp_item_price, temp_item_quantity = item[temp_item_key]
                print(f"{temp_item_key:<23} | {temp_item_price:<10} | {temp_item_quantity:<10}")
            print(receipt_divider)

            # Ask the user if they are ready to pay and handle their response
            ready_receipt = input("Are you ready to pay? (Y)es or enter anything else to go back: ").upper()
            if ready_receipt == "Y":
                # Calculate the total price using list comprehension
                total_price = sum(price * quantity for item in order_list for price, quantity in item.values())
                print(f"Your total is ${total_price:.2f}")
                print("Thank you for your purchase!")
                break
        case _:
            continue
