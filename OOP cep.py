import time
import datetime
x = "user_information.txt"

class User:
    def __init__(self, first_name, last_name, contact, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.email = email
        self.username = username
        self.password = password

    @staticmethod
    def read_user_data():
        users = []
        with open(x, 'r') as file:
            lines = file.readlines()
            for line in lines:
                stored_username, stored_password = (part.strip() for part in line.split(':'))
                users.append(User(None, None, None, None, stored_username, stored_password))
        return users

    @staticmethod
    def is_username_taken(username):
        with open(x, 'r') as file:
            lines = file.readlines()
            existing_usernames = [line.split(':')[0].strip() for line in lines]
        return username in existing_usernames

    @staticmethod
    def signup():
        while True:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            contact = input("Enter your contact no: ")
            email = input("Enter your email: ")
            username = input("Enter your username: ").strip()

            if len(username) < 4:
                print('Please enter a username of 4 or more characters')
                continue

            if User.is_username_taken(username):
                print("Username is already taken. Please choose a different username.")
                continue

            while True:
                password = input("Password must be at least 8 characters, including one uppercase letter, one lowercase letter, and one digit.\nEnter your password: ")

                if len(password) < 8 or not any(char.islower() for char in password) or not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
                    continue

                with open(x, 'a') as file:
                    file.write(f"{username}:{password}\n")

                print("Signup successful!")
                return

    @staticmethod
    def login():
        users = User.read_user_data()
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            for user in users:
                if username == user.username and password == user.password:
                    print("Login successful!")
                    return user

            print("Invalid username or password. Please try again.")
            print("Options:")
            print("1. Go to Signup")
            print("2. Retry Login")

            option = input("Enter your choice: ")

            if option == '1':
                User.signup()
                return None
            elif option == '2':
                continue
            else:
                print("Invalid option. Please try again.")

class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, item, quantity):
        if quantity > item['quantity']:
            print(f"Sorry, only {item['quantity']} {item['name']} available.")
        else:
            self.cart.append({"item": item, "quantity": quantity})
            item['quantity'] -= quantity
            print(f"Specific details: {item['details']}")
            print(f"{quantity} {item['name']} added to the cart.")

    def remove_from_cart(self, item_name):
        for cart_item in self.cart:
            if cart_item['item']['name'].lower() == item_name.lower():
                remove_quantity = int(input(f"How many {item_name} do you want to remove from the cart? "))
                if remove_quantity >= cart_item['quantity']:
                    self.cart.remove(cart_item)
                    cart_item['item']['quantity'] += cart_item['quantity']
                    print(f"All {cart_item['quantity']} {item_name} removed from the cart.")
                else:
                    cart_item['quantity'] -= remove_quantity
                    cart_item['item']['quantity'] += remove_quantity
                    print(f"{remove_quantity} {item_name} removed from the cart.")
                return
        print(f"{item_name} not found in the cart.")

    def display_cart(self):
        if not self.cart:
            print("\nCart is empty\n")
        else:
            print("Items in your cart:")
            for cart_item in self.cart:
                print(f"{cart_item['quantity']} {cart_item['item']['name']} - ${cart_item['item']['price']} each")

    def view_order_history(self):
        with open('user_history.txt', 'a') as f:
            if self.cart:
                print('Your order history:')
                for cart_item in self.cart:
                    print(f"{cart_item['item']['name']} - Quantity of the item ordered: {cart_item['quantity']}")
                print(f"Total: ${sum(cart_item['item']['price'] * cart_item['quantity'] for cart_item in self.cart)}")
                current_time = time.strftime("%H:%M:%S")
                current_date = datetime.date.today()
                print("Time:", current_time)
                print("Date:", current_date)

    def order_history(self):
        with open('user_history.txt', 'a+') as f:
            for cart_item in self.cart:
                f.write(str(cart_item) + ' ')

    def checkout(self):
        print("\nCheckout - Total Bill:")
        total_bill = sum(cart_item['item']['price'] * cart_item['quantity'] for cart_item in self.cart)
        for cart_item in self.cart:
            print(f"{cart_item['quantity']} {cart_item['item']['name']} - ${cart_item['item']['price']} each")
        print('\n')
        print(f"Total: ${total_bill}")
        print("\nThank you for shopping with us!")

class Supermarket:
    def __init__(self):
        self.shopping_cart = ShoppingCart()
        self.menu = {
            1: {"name": "Laptop", "price": 1000, "details": "High-performance laptop.", "quantity": 10},
            2: {"name": "Headphones", "price": 20, "details": "Noise-canceling headphones.", "quantity": 10},
            3: {"name": "Smartphone", "price": 500, "details": "Latest smartphone model.", "quantity": 10},
            4: {"name": "Backpack", "price": 50, "details": "Durable and spacious backpack.", "quantity": 10},
            5: {"name": "Smartwatch", "price": 150, "details": "Elegant wristwatch.", "quantity": 10},
            6: {"name": "Tablet", "price": 700, "details": "Smart and sleek.", "quantity": 10},
            7: {"name": "Stylus", "price": 30, "details": "Pen re-imagined with a greater battery life.", "quantity": 10},
            8: {"name": "Graphic tablet", "price": 125, "details": "With better precision sensors.", "quantity": 10},
            9: {"name": "Projector", "price": 300, "details": "16M vivid and true colors.", "quantity": 10},
            10: {"name": "Keyboard", "price": 25, "details": "Soft keys with backlit background.", "quantity": 10}
        }

    def display_menu(self):
        print("\nShopping Menu:")
        for key, item in self.menu.items():
            print(f"{key}. {item['name']} - ${item['price']} each (Quantity: {item['quantity']})")

    def cart_menu(self):
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
                self.display_menu()
            elif choice == '2':
                self.shopping_cart.display_cart()
                self.display_menu()
                add_choice = int(input("Enter the item number to add to the cart: "))
                if 1 <= add_choice <= len(self.menu):
                    selected_item = self.menu[add_choice]
                    quantity = int(input(f"How many {selected_item['name']} do you want to purchase? "))
                    self.shopping_cart.add_to_cart(selected_item, quantity)
                else:
                    print("Invalid input. Please enter a valid item number.")
            elif choice == '3':
                self.shopping_cart.display_cart()
                remove_choice = input("Enter the name of the item to remove from the cart: ")
                self.shopping_cart.remove_from_cart(remove_choice)
            elif choice == '4':
                self.shopping_cart.display_cart()
            elif choice == '5':
                self.shopping_cart.checkout()
                self.shopping_cart.order_history()
            elif choice == '6':
                self.shopping_cart.view_order_history()
            else:
                print("Invalid input. Please enter a valid option.")

def main_menu():
    supermarket = Supermarket()
    while True:
        print('''
            *WELCOME TO THE AMO STORE*
              Please choose an option:  
               1. Signup
               2. Login
               0. Exit''')
        y = input('Enter choice: ')
        if y == "1":
            User.signup()
        elif y == "2":
            user = User.login()
            if user:
                supermarket.cart_menu()
        elif y == "0":
            break
        else:
            print('Invalid choice')

main_menu()
