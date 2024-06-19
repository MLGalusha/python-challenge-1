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

def check_valid_num(list, question):
    # Prompt user to pick one of the categories and check if number is valid
    while True:
        user_choice = input(question)
        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= len(list):
                return user_choice
            else:
                print(f"Please enter a number between 1 and {len(list)}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# UNIVERSAL THINGS
header = f"{'ITEM #':<6} | {'ITEM':<23} | {'PRICE':<10}"
divider = "-" * len(header)
order_list = []
total_price = 0

print("Welcome to the variety food truck.")

# Create a loop that only ends when user is done ordering
while True:

    # Print food categories with corresponding values
    category_list = [key for key in menu.keys()]
    for idx, item in enumerate(category_list, start=1):
        print(f"{idx}. {item}")

    # Prompt user to pick one of the categories and check if number is valid
    cat_question = "Which category would you like to pick? "
    user_category = check_valid_num(category_list, cat_question)

    print(f"{divider}\n{header}\n{divider}")
    i = 1
    item_list = []
    for item, price in menu[category_list[user_category - 1]].items():
        if isinstance(price, dict):
            for item_sub, price_sub in price.items():
                item_list.append({f"{item} - {item_sub}": price_sub})
                print(f"{i:<6} | {f'{item} - {item_sub}':<23} | {price_sub:<10}")
                i += 1
        else:
            item_list.append({item: price})
            print(f"{i:<6} | {item:<23} | {price:<10}")
            i += 1
    print(divider)

    # Ask which item the user wants to order
    item_question = "Which item would you like to order?  "
    item_num = check_valid_num(item_list, item_question)

    while True:
        the_item = item_list[item_num - 1]
        the_key = list(the_item.keys())[0]
        quantity = input(f"How many {the_key}s would you like to order? ")
        if quantity.isdigit() and int(quantity) >= 1:
            quantity = int(quantity)
            break
        else:
            print("Invalid input. Please type a valid number.\n")

    # Create a temporary dictionary to store the order and calculate the total price
    tkey, tprice = next(iter(the_item.items()))
    temp_dict = {tkey: [tprice, quantity]}
    total_price += tprice * quantity
    order_list.append(temp_dict)

    # Check if user wants to keep ordering
    still_ordering = input("\nAre you still ordering? (N)o or enter anything else to continue ordering: ")
    if still_ordering.upper() == "N":
        receipt_header = f"{'ITEM':<23} | {'PRICE':<10} | {'QUANTITY':<10}"
        receipt_divider = "-" * len(receipt_header)
        print(receipt_divider)
        print(f"{'RECEIPT':^46}")
        print(receipt_divider)
        print(receipt_header)
        print(receipt_divider)

        # Unpack the list and dictionary into three separate pieces of data
        for item in order_list:
            temp_item_key = list(item.keys())[0]
            temp_item_price, temp_item_quantity = item[temp_item_key]
            print(f"{temp_item_key:<23} | {temp_item_price:<10} | {temp_item_quantity:<10}")
        print(receipt_divider)

        ready_receipt = input("Are you ready to pay? (Y)es or enter anything else to go back: ").upper()
        if ready_receipt == "Y":
            print(f"Your total is ${total_price:.2f}")
            print("Thank you for your purchase!")
            break
        else:
            continue
    else:
        print("continue")
        continue
