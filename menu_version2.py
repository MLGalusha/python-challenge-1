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

# UNIVERSAL THINGS
total_price = 0
order_list = []

def display_categories(menu):
    category_list = [key for key in menu.keys()]
    for idx, item in enumerate(category_list, start=1):
        print(f"{idx}. {item}")
    return category_list

def check_valid_num(list, question, context_function=None, context_args=None):
    while True:
        if context_function:
            context_function(*context_args)
        user_choice = input(question).upper()
        if user_choice == 'B':
            return 'B'
        elif user_choice == 'L':
            return 'L'
        elif user_choice == 'F':
            return 'F'
        elif user_choice == 'V':
            return 'V'
        elif user_choice == 'HELP':
            display_help()
            continue
        try:
            user_choice = int(user_choice)
            if 1 <= user_choice <= len(list):
                return user_choice
            else:
                print(f"Please enter a number between 1 and {len(list)}.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or command.\n")

def display_items(category, menu):
    header = f"{'ITEM #':<6} | {'ITEM':<23} | {'PRICE':<10}"
    divider = "-" * len(header)
    print(f"{divider}\n{header}\n{divider}")

    i = 1
    item_list = []
    for item, price in menu[category].items():
        if isinstance(price, dict):
            for item_sub, price_sub in price.items():
                item_list.append({f"{item} - {item_sub}": price_sub})
                print(f"{i:<6} | {f'{item} - {item_sub}':<23} | ${price_sub:<9.2f}")
                i += 1
        else:
            item_list.append({item: price})
            print(f"{i:<6} | {item:<23} | ${price:<9.2f}")
            i += 1
    print(divider)
    return item_list

def get_user_order(item_list, category):
    item_question = "Which item would you like to order? (or 'B' to go back, 'L' to leave, 'F' to finish, 'V' to view cart, 'HELP' for help): "
    item_num = check_valid_num(item_list, item_question, lambda: None, ())

    if item_num in ['B', 'L', 'F', 'V']:
        return item_num

    while True:
        the_item = item_list[item_num - 1]
        the_key = list(the_item.keys())[0]
        quantity = input(f"How many {the_key}s would you like to order? ")
        if quantity.isdigit() and int(quantity) >= 1:
            quantity = int(quantity)
            break
        else:
            print("Invalid input. Please type a valid number.\n")

    special_instructions = input("Any special instructions? (Press Enter if none): ")

    tkey, tprice = next(iter(the_item.items()))
    return {tkey: [tprice, quantity, special_instructions]}

def print_receipt(order_list):
    receipt_header = f"{'ITEM':<23} | {'PRICE':<10} | {'QUANTITY':<10} | {'TOTAL':<10} | {'INSTRUCTIONS':<20}"
    receipt_divider = "-" * len(receipt_header)
    print(receipt_divider)
    print(f"{'RECEIPT':^{len(receipt_header)}}")
    print(receipt_divider)
    print(receipt_header)
    print(receipt_divider)

    total_price = 0
    for item in order_list:
        temp_item_key = list(item.keys())[0]
        temp_item_price, temp_item_quantity, temp_item_instructions = item[temp_item_key]
        item_total = temp_item_price * temp_item_quantity
        total_price += item_total
        print(f"{temp_item_key:<23} | ${temp_item_price:<9.2f} | {temp_item_quantity:<10} | ${item_total:<9.2f} | {temp_item_instructions[:20]:<20}")
    print(receipt_divider)
    print(f"{'TOTAL:':<46}${total_price:.2f}")
    print(receipt_divider)
    return total_price

def modify_order(order_list):
    print("\nCurrent Order:")
    for i, item in enumerate(order_list, 1):
        item_name = list(item.keys())[0]
        quantity = item[item_name][1]
        print(f"{i}. {item_name} - Quantity: {quantity}")

    while True:
        choice = input("\nEnter the number of the item you want to modify (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(order_list):
                item = order_list[choice - 1]
                item_name = list(item.keys())[0]
                new_quantity = input(f"Enter new quantity for {item_name} (0 to remove): ")
                if new_quantity.isdigit():
                    new_quantity = int(new_quantity)
                    if new_quantity == 0:
                        order_list.pop(choice - 1)
                        print(f"{item_name} removed from order.")
                    else:
                        item[item_name][1] = new_quantity
                        print(f"{item_name} quantity updated to {new_quantity}.")
                else:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

def process_payment(total_price):
    print(f"\nTotal amount due: ${total_price:.2f}")
    paid_amount = 0
    valid_bills = [100, 50, 20, 10, 5, 1]
    valid_coins = [0.25, 0.10, 0.05, 0.01]

    while paid_amount < total_price:
        payment = input("Enter the amount you're paying (e.g., 20 for $20 bill, 0.25 for quarter): ")
        try:
            payment = float(payment)
            if payment in valid_bills or payment in valid_coins:
                paid_amount += payment
                print(f"Received: ${payment:.2f}")
                print(f"Total paid: ${paid_amount:.2f}")
                print(f"Remaining: ${max(0, total_price - paid_amount):.2f}")
            else:
                print("Invalid denomination. Please use valid bills or coins.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    change = paid_amount - total_price
    if change > 0:
        print(f"\nChange due: ${change:.2f}")
        calculate_change(change)

    print("Thank you for your payment!")

def calculate_change(change):
    denominations = [100, 50, 20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    for denom in denominations:
        if change >= denom:
            count = int(change // denom)
            print(f"{count} x ${denom:.2f}")
            change = round(change % denom, 2)

def check_duplicate_items(order_list, new_item):
    new_item_name = list(new_item.keys())[0]
    for item in order_list:
        item_name = list(item.keys())[0]
        if item_name == new_item_name:
            item[item_name][1] += new_item[new_item_name][1]
            return True
    return False

def view_cart(order_list):
    if not order_list:
        print("\nYour cart is empty.")
    else:
        print("\nCurrent Cart:")
        for item in order_list:
            item_name = list(item.keys())[0]
            price, quantity, instructions = item[item_name]
            print(f"{item_name} - Quantity: {quantity}, Price: ${price:.2f}, Instructions: {instructions}")

def display_help():
    header = f"{'HELP MENU':^35}"
    divider = "-"*(len(header))
    print(f"|{divider}|\n|{header}|\n|{divider}|")
    print(f'| Type: "B" to back out of category |\n|{" "*len(header)}|')
    print(f'| Type: "C" to cancel your order    |\n|{" "*len(header)}|')
    print(f'| Type: "V" to view your cart       |\n|{" "*len(header)}|')
    print(f'| Type: "F" to finish your order    |\n|{" "*len(header)}|')
    print(f'| Type: "HELP" to see the help menu |\n|{divider}|')
    input(f"|{' ':35}|\n|{'ENTER ANYTHING TO RETURN':^35}|\n|{' ':35}|\n|{divider}|\n")


def main():
    global order_list
    print("Welcome to the variety food truck.")

    while True:
        category_list = display_categories(menu)
        cat_question = "Which category would you like to pick? (or 'L' to leave, 'F' to finish, 'V' to view cart, 'HELP' for help): "
        user_category = check_valid_num(category_list, cat_question, lambda: None, ())

        if user_category == 'L':
            print("Thank you for visiting. Have a great day!")
            return
        elif user_category == 'F':
            if confirm_finish():
                break
            else:
                continue
        elif user_category == 'V':
            view_cart(order_list)
            continue

        item_list = display_items((category_list[user_category - 1]), menu)
        order = get_user_order(item_list, category_list[user_category - 1])

        if order == 'B':
            continue
        elif order == 'L':
            print("Thank you for visiting. Have a great day!")
            return
        elif order == 'F':
            if confirm_finish():
                break
            else:
                continue
        elif order == 'V':
            view_cart(order_list)
            continue

        if not check_duplicate_items(order_list, order):
            order_list.append(order)

def confirm_finish():
    confirm = input("Are you sure you want to finish ordering? (Y/N): ").upper()
    return confirm == 'Y'

if __name__ =="__main__":
    main()