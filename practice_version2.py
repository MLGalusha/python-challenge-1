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

def check_valid_num(list, question):
    """
    Prompt the user with a question and check if the input is a valid number within the range of the provided list.
    Returns the valid user input.
    """
    while True:
        user_choice = input(question).upper()
        try:
            user_choice = int(user_choice)
            if 1<= user_choice <= len(list):
                return user_choice
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(list)}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

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
    item_num = check_valid_num(item_list, question)

    while True:
        item = item_list[item_num - 1]
        key = list(item.keys())[0]
        quantity = check_valid_num(list(range(1, 201)), f"How many {key}s would you like to order? ")
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
        return "Finish"
    else:
        return

def main():
    global order_list
    global total_price
    print("Welcome to the variety food truck. ")

    while True:
        category_list = display_categories(menu)
        category_question = "Which category would you like to pick? "
        user_category = check_valid_num(category_list, category_question)

        item_list = display_items((category_list[user_category - 1]), menu)
        order = get_user_order(item_list, category_list[user_category - 1])
        order_list.append(order)

        keep_ordering = input("Do you want to keep ordering? (N)o or enter anything to continue: ")
        if keep_ordering.upper() == 'N':
            print_receipt()
            if confirm_finish() != None:
                break
            else:
                continue




if __name__ =="__main__":
    main()