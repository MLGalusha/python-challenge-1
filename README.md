# Food Truck Ordering System

## Code Explaination
<details>
  <summary>Menu Dictionary</summary>

  ```python
  # This is a nested dictionary containg the entire food truck menu
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
```
</details>
## Steps to Implement the Ordering System
### Pseudocode

1. **Create a Dictionary for Menu:**
   - Add a dictionary containing types of foods.
   - Each type of food will have a sub-dictionary with food items and their prices.

2. **Display Menu to User:**
   - Print the menu of food types with numbers representing each category.

3. **User Input for Food Category:**
   - Ask the user to choose a category by inputting a number.
   - Validate the input to ensure it is a valid number.

4. **Display Items in Selected Category:**
   - If the input is valid, print the list of items within the chosen category.
   - Show the item number, item name, and price.

5. **User Input for Specific Item:**
   - Have the user pick an item by inputting the item number.
   - Validate the input to ensure it is a valid number.
   - If the user inputs nothing, prompt them to confirm if they are done ordering:
     - If they type "y", end the order.
     - Otherwise, continue with the order.

6. **Print Receipt:**
   - Once the order is ended, print out the receipt dynamically.
   - Display the item name, corresponding price, and quantity.

7. **Calculate and Display Total Price:**
   - Add up the total price and print it out for the user to see.

## Possible Additions

1. **Modify Order:**
   - Ask if everything on the receipt looks correct.
   - If the user responds with "no":
     - Ask which item they would like to modify.
     - Allow them to type the item name and the new quantity.
     - If the quantity is 0, delete the item from the receipt.

2. **Payment Process:**
   - Ask the customer if they are ready to pay.
   - If they say "yes", reprint the modified receipt and prices.
   - Allow the user to pay with cash:
     - Accept dollar bills: 1, 5, 10, 20, 50, 100.
     - Accept cents: 0.01, 0.05, 0.10, 0.25.
   - If they give too much, print out their change.
