import sys

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

# UNIVERSAL
order_list = []
total_price = 0

def display_categories(menu):
    """Display all categories from the menu."""
    category_list = [key for key in menu.keys()]
    for idx, item in enumerate(category_list, start=1):
        print(f"{idx}. {item}")
    return category_list

def _reprint(context_function, context_arg=None):
    """Helper Function: Reprints the prompt user was currently on"""
    if context_arg:
        context_function(context_arg, menu)
        return
    try:
        context_function(menu)
        return
    except TypeError:
        return

def _cancel_order():
    """Asks user if they are sure they want to cancel order. Responds accordingly"""
    cancel = input("Type (C) to confirm canceling order. ")
    if cancel.upper() == "C":
        print("Bye have a great day!")
        sys.exit()


def check_valid_input(question, list=None, context_function=None, context_arg=None):
    """
    Prompt the user with a question and check if the input is a valid
    If list provided in argument check if input is a valid number within the range of the provided list.
    Returns the valid user input.
    """
    global total_price

    while True:
        user_choice = input(question)
        match user_choice.upper():
            case "B":
                if question == "Which category would you like to pick? ":
                    print("You can't go back anymore.")
                    continue
                back_out = input("Type (B) to confirm and go back to menu categories. ")
                if back_out.upper() == "B":
                    return "B"
                _reprint(context_function, context_arg)
                continue
            case "C":
                _cancel_order()
                _reprint(context_function, context_arg)
                continue
            case "V":
                print_receipt()
                print(" ")
                _reprint(context_function, context_arg)
                continue
            case "F":
                if total_price == 0:
                    _cancel_order()
                print_receipt()
                confirm_finish()
                _reprint(context_function, context_arg)
                continue
            case "HELP":
                display_help()
                _reprint(context_function, context_arg)
                continue
        if list:
            try:
                user_choice = int(user_choice)
                if 1<= user_choice <= len(list):
                    return user_choice
                else:
                    print(f"Invalid input. Please enter a number between 1 and {len(list)}.\n")
            except ValueError:
                print("Invalid input. Please enter a valid number.\n")
                if context_function == display_categories:
                    _reprint(context_function(menu))

        else:
            return user_choice

def display_items(category, menu):
    """
    Display all items in the specified category of the menu.
    Returns a list of items in the category in order.
    """
    header = f'{"ITEM #":<6} | {"ITEM":<23} | {"PRICE":<10}'
    divider = "-"*len(header)
    print(f"{divider}\n{header}\n{divider}")

    item_list = []
    i = 1
    for key, value in menu[category].items():
        if type(value) is dict:
            for item, price in value.items():
                item_list.append({f"{key} - {item}": price})
                print(f"{i:<6} | {f'{key} - {item}':<23} | {price:<9.2f}")
                i += 1
        else:
            item_list.append({key: value})
            print(f"{i:<6} | {key:<23} | {value:<9.2f}")
            i += 1
    print(divider)
    return item_list

def get_user_order(item_list, category):
    """
    Prompt the user to select an item from the list and specify the quantity.
    Returns a dictionary representing the selected item and its quantity.
    """
    global total_price
    question = "Which item would you like to order? "
    item_num = check_valid_input(question, item_list, display_items, category)
    if item_num == "B":
        return item_num
    while True:
        item = item_list[item_num - 1]
        key = list(item.keys())[0]
        quantity = check_valid_input(f"How many {key}s would you like to order? ", list(range(1, 201)))
        if quantity == "B":
            return quantity
        if quantity:
            break

    key, price = next(iter(item.items()))
    total_price += price * quantity
    return {key: [price, quantity]}

def print_receipt():
    """
    Print a receipt of all items in the global order_list with their quantities and prices.
    """
    global order_list
    header = f"{'ITEM':<23} | {'PRICE':<7} | {'QUANTITY':<10}"

    divider = "-"*len(header)
    print(f"{divider}\n{'RECEIPT':^36}\n{divider}\n{header}\n{divider}")

    for item in order_list:
        for name, data in item.items():
                price, quantity = data
                print(f"{name:<23} | {price:<7} | {quantity:<10}")
    print(divider)

def confirm_finish():
    """
    Ask the user if they are finished ordering.
    If confirmed, print the total price and end the ordering process.
    """
    global total_price

    confirm = input("Are you sure you want to finish ordering? (Y)es or enter anything to keep ordering: ")
    if confirm.upper() == 'Y':
        print(f"Your total is ${total_price:,.2f}\nThank you for ordering! Have a great day!")
        sys.exit()
    else:
        return

def display_help():
    header = f"{'HELP MENU':^35}"
    divider = "-"*(len(header))
    print(f"|{divider}|\n|{header}|\n|{divider}|")
    print(f'| Type: "B" to back out of category |\n|{" "*len(header)}|')
    print(f'| Type: "C" to cancel your order    |\n|{" "*len(header)}|')
    print(f'| Type: "V" to view your cart       |\n|{" "*len(header)}|')
    print(f'| Type: "F" to finish your order    |\n|{" "*len(header)}|')
    print(f'| Type: "HELP" to see the help menu |\n|{divider}|')
    input(f"|{' ':35}|\n|{'ENTER ANYTHING TO CONTINUE':^35}|\n|{' ':35}|\n|{divider}|\n")


def main():
    global order_list
    global total_price
    print("Welcome to the variety food truck. ")

    while True:
        category_list = display_categories(menu)
        user_category = check_valid_input("Which category would you like to pick? ", category_list, display_categories)
        if user_category == "B":
            continue

        item_list = display_items((category_list[user_category - 1]), menu)
        order = get_user_order(item_list, category_list[user_category - 1])
        if order == "B":
            continue

        order_list.append(order)
        keep_ordering = check_valid_input("Do you want to keep ordering? (N)o or enter anything to continue: ")
        if keep_ordering.upper() == 'N':
            print_receipt()
            confirm_finish()
            continue


if __name__ =="__main__":
    main()
