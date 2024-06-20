# Food Truck Ordering System


<details>
  <summary><h2> ∆ Original Pseudocode ∆<h2></summary>

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
</details>

## Possible Additions

1. **Modify Order:**
   - After displaying the receipt, ask if everything looks correct.
   - If the user responds with "no":
     - Ask which item they would like to modify.
     - Allow them to type the item name and the new quantity.
     - If the quantity is 0, remove the item from the receipt.
     - If the quantity is more than 0, update the item quantity accordingly.

2. **Payment Process:**
   - Ask the customer if they are ready to pay.
   - If they say "yes", reprint the final receipt with updated prices.
   - Allow the user to pay with cash:
     - Accept dollar bills: 1, 5, 10, 20, 50, 100.
     - Accept coins: 0.01, 0.05, 0.10, 0.25.
   - If they provide too much money, calculate and print out their change.

3. **Check Duplicate Items:**
   - When an item is added to the cart, check if it is already in the cart.
   - If it is, update the quantity of the existing item instead of adding a duplicate.
   - This prevents duplicate items on the receipt and keeps the order organized.

4. **Add "Back Out" of Menu Category:**
   - Allow the user to input "B" to back out of a menu category if they don't want to order anything from it.
   - This provides flexibility for users who may change their mind after selecting a category.

5. **Cancel or End Anytime:**
   - Provide an option to cancel the order at any time by inputting "L" to leave.
   - Display a thank you message when the user leaves without completing the order.
   - Allow users to finish their order anytime by inputting "F".
   - If the user inputs "F", confirm if they are sure they are done ordering.
   - If they confirm by typing "Y", skip to displaying the receipt.

6. **View Cart:**
   - Allow users to view their current cart at any time by inputting "V".
   - This helps users keep track of their order and make adjustments if necessary.

7. **Special Instructions:**
   - Provide an option for users to add special instructions for their order (e.g., no onions, extra cheese).
   - This can be done after selecting the quantity of an item.

8. **HELP:**
   - Allow the user to type "help" at any time to display a help menu.
   - The help menu will show all available options and how to use them.
   - Explain what each input does, such as:
     - "B" to back out of a category
     - "L" to cancel the order
     - "F" to finish ordering
     - etc....
   - These inputs can be used at any time during the ordering process.
   - If the user types "help" while in the middle of ordering, they can press "return" or any other unused key to return to where they left off.
