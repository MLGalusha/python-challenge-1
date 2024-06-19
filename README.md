# Food Truck Ordering System

## Steps to Implement the Ordering System

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
