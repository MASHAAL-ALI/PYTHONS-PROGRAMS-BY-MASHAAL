x = 'user_information.txt'  # Set the global variable for the file path
print('''
               ***       ***  ********** ***       ********* *********  *************** **********
               ***  ***  ***  *********  ***       ********* *********  *************** *********
               ***  ***  ***  ***        ***       ***       ***   ***  ***   ***   *** ***
               ***  ***  ***  ******     ***       ***       ***   ***  ***   ***   *** ******
               ***  ***  ***  ******     ***       ***       ***   ***  ***   ***   *** ******
               ***  ***  ***  ***        ***       ***       ***   ***  ***   ***   *** ***
               *************  *********  ********* ********* *********  ***   ***   *** *********
               *************  ********** ********* ********* *********  ***         *** **********
               
                                        ************* ***********
                                        ************* ***********
                                             ***      ***     ***
                                             ***      ***     ***
                                             ***      ***     ***                                
                                             ***      ***     ***
                                             ***      ***     ***
                                             ***      ***********
                                             ***      ***********

        ************ *************** ************    ********** ********** ********** **********  *********
        ************ *************** ************    ********** ********** ********** **********  ********
        ****    **** ***   ***   *** ***      ***    ***            ***    ***    *** **      **  *** 
        ****    **** ***   ***   *** ***      ***    ***            ***    ***    *** **      **  ******
        ************ ***   ***   *** ***      ***    **********     ***    ***    *** **********  ******
        ************ ***   ***   *** ***      ***    **********     ***    ***    *** **********  ***
        ***      *** ***   ***   *** ***      ***           ***     ***    ***    *** **     ***  ***
        ***      *** ***   ***   *** ************    **********     ***    ********** **      *** ********
        ***      *** ***         *** ************    **********     ***    ********** **       ** *********

''')

def read_user_data():
    # Function to read user data from the file
    users_data = []

    with open(x, 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = (part.strip() for part in line.split(':'))
            user_data = {'username': stored_username, 'password': stored_password}
            users_data.append(user_data)

    return users_data

def login():
    # Function to handle user login
    users_data = read_user_data()

    while True:
        print()
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the entered username and password match the signup data
        for user_data in users_data:
            if username == user_data['username'] and password == user_data['password']:
                print("Login successful!")
                return

        print("Invalid username or password. Please try again.")
        print("Options:")
        print("1. Go to Signup")
        print("2. Retry Login")

        option = input("Enter your choice: ")

        if option == '1':
            signup()
            return  # Return to the main menu after signup
        elif option == '2':
            continue  # Retry login
        else:
            print("Invalid option. Please try again.")

# Example usage

def is_username_taken(username):
    # Function to check if a username is already taken
    with open(x, 'r') as file:
        lines = file.readlines()
        existing_usernames = [line.split(':')[0].strip() for line in lines]
    return username in existing_usernames

def signup():
    # Function to handle user signup
    while True:
        # Get user input
        username = input("Enter your username: ").strip()
        if len(username) < 4:
            print('Please enter a username of 4 or more than 4 characters')
            continue

        # Check if the username is already taken
        if is_username_taken(username):
            print("Username is already taken. Please choose a different username.")
            continue  # Continue to the next iteration of the loop if the username is taken

        while True:
            password = input("Password must be at least 8 characters, including one uppercase letter, one lowercase letter, and one digit.\nEnter your password: ")

            # Validate password (at least 8 characters, one uppercase, one lowercase, one digit)
            if len(password) < 8 or not any(char.islower() for char in password) \
                    or not any(char.isupper() for char in password) \
                    or not any(char.isdigit() for char in password):
                continue  # Continue to the next iteration of the password loop if the password is invalid

            # Save username and password to a file (append mode)
            with open(x, 'a') as file:
                file.write(f"{username}:{password}\n")

            print("Signup successful!")
            return  # Exit the function once signup is successful

def add_to_cart(cart, item, quantity):
    # Function to add items to the shopping cart
    if quantity > item['quantity']:
        print(f"Sorry, only {item['quantity']} {item['name']} available.")
    else:
        cart.append({"item": item, "quantity": quantity})
        item['quantity'] -= quantity
        print(f"Specific details: {item['details']}")
        print(f"{quantity} {item['name']} added to the cart.")

def remove_from_cart(cart, item_name):
    # Function to remove items from the shopping cart
    for cart_item in cart:
        if cart_item['item']['name'].lower() == item_name.lower():
            remove_quantity = int(input(f"How many {item_name} do you want to remove from the cart? "))
            if remove_quantity >= cart_item['quantity']:
                cart.remove(cart_item)
                cart_item['item']['quantity'] += cart_item['quantity']
                print(f"All {cart_item['quantity']} {item_name} removed from the cart.")
            else:
                cart_item['quantity'] -= remove_quantity
                cart_item['item']['quantity'] += remove_quantity
                print(f"{remove_quantity} {item_name} removed from the cart.")
            return
    print(f"{item_name} not found in the cart.")

def display_cart(cart):
    # Function to display items in the shopping cart
    if not cart:
        print("\n")
        print("cart is empty")
        print('\n')
    else:
        print("Items in your cart:")
        for cart_item in cart:
            print(f"{cart_item['quantity']} {cart_item['item']['name']} - ${cart_item['item']['price']} each")

import time
import datetime

def view_order_history(cart):
    # Function to view order history
    with open('user_history.txt', 'a') as f:
        if cart:
            print('Your order history:')
            for cart_item in cart:
                print(f"{cart_item['item']['name']} - Quantity of the item ordered: {cart_item['quantity']}")
            print(f"Total: ${sum(cart_item['item']['price'] * cart_item['quantity'] for cart_item in cart)}")
            current_time = time.strftime("%H:%M:%S")
            current_date = datetime.date.today()
            print("Time:", current_time)
            print("Date:", current_date)

def order_history(cart):
    # Function to log order history
    with open('user_history.txt', 'a+') as f:
        for cart_item in cart:
            f.write(str(cart_item) + ' ')

def checkout(cart):
    # Function to handle the checkout process
    print("\nCheckout - Total Bill:")
    total_bill = sum(cart_item['item']['price'] * cart_item['quantity'] for cart_item in cart)
    for cart_item in cart:
        print(f"{cart_item['quantity']} {cart_item['item']['name']} - ${cart_item['item']['price']} each")
    print('\n')
    print(f"Total: ${total_bill}")
    print("\nThank you for shopping with us!")

def cart_menu():
    # Function to display the shopping menu and manage the shopping cart
    shopping_cart = []
    menu = {
        1: {"name": "Laptop", "price": 1000, "details": "High-performance laptop.", "quantity": 10},
        2: {"name": "Headphones", "price": 20, "details": "Noise-canceling headphones.", "quantity": 10},
        3: {"name": "Smartphone", "price": 500, "details": "Latest smartphone model.", "quantity": 10},
        4: {"name": "Backpack", "price": 50, "details": "Durable and spacious backpack.", "quantity": 10},
        5: {"name": "Smartwatch", "price": 150, "details": "Elegant wristwatch.", "quantity": 10},
        6: {"name": "Tablet", "price": 700, "details": "Smart and sleek.", "quantity": 10},
        7: {"name": "Stylus", "price": 30, "details": "pen re-imagined with a greater battery life", "quantity": 10},
        8: {"name": "Graphic tablet", "price": 125, "details": "With better precision sensors.", "quantity": 10},
        9: {"name": "Projector", "price": 300, "details": "16M vivid and true colors.", "quantity": 10},
        10: {"name": "Keyboard", "price": 25, "details": "Soft keys with backlit background.", "quantity": 10}
    }

    while True:
         print("\nMenu:")
         print("1. Display Shopping Menu")
         print("2. Add Item to Cart")
         print("3. Remove Item from Cart")
         print("4. View Cart")
         print("5. Checkout")
         print("6. View history")
         print("0. Exit")

         choice = input("Enter your choice: ")

         if choice == '0':
            break
         if choice == '1':
             print("\nShopping Menu:")
             for key, item in menu.items():
                 print(f"{key}. {item['name']} - ${item['price']} each (Quantity: {item['quantity']})")
         elif choice == '2':
             display_cart(shopping_cart)
             for key, item in menu.items():
                 print(f"{key}. {item['name']} - ${item['price']} each (Quantity: {item['quantity']})")
             add_choice = int(input("Enter the item number to add to the cart: "))
             if 1 <= add_choice <= len(menu):
                 selected_item = menu[add_choice]
                 quantity = int(input(f"How many {selected_item['name']} do you want to purchase? "))
                 add_to_cart(shopping_cart, selected_item, quantity)
             else:
                 print("Invalid input. Please enter a valid item number.")
         elif choice == '3':
             display_cart(shopping_cart)
             remove_choice = input("Enter the name of the item to remove from the cart: ")
             remove_from_cart(shopping_cart, remove_choice)
         elif choice == '4':
             display_cart(shopping_cart)
         elif choice == '5':
             checkout(shopping_cart)
             order_history(shopping_cart)
         elif choice == '6':
             view_order_history(shopping_cart)
         else:
             print("Invalid input. Please enter a valid option.")

# Example usage
def main_menu():
    # Function to display the main menu and manage user choices
    while True:
        print('''
            *WELCOME TO THE AMO STORE*
              Please choose an option:  
               1. Signup
               2. Login
               0. Exit''')
        y = (input('Enter choice: '))
        if y == "1":
            signup()
        elif y == "2":
            login()
            cart_menu()
        elif y == "0":
            break
        else:
            print('Invalid choice')

main_menu()