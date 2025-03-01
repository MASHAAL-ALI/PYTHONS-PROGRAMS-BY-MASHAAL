def add_to_cart(cart, item):
    cart.append(item)
    print(f"{item['name']} added to the cart.")

def remove_from_cart(cart, item_name):
    for item in cart:
        if item['name'].lower() == item_name.lower():
            cart.remove(item)
            print(f"{item_name} removed from the cart.")
            return
    print(f"{item_name} not found in the cart.")

def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in cart:
            print(f"{item['name']} - ${item['price']}")

def cart_menu():
    shopping_cart = []
    menu = {
        1: {"name": "Laptop", "price": 1000, "details": "High-performance laptop."},
        2: {"name": "Headphones", "price": 100, "details": "Noise-canceling headphones."},
        3: {"name": "Smartphone", "price": 500, "details": "Latest smartphone model."},
        4: {"name": "Backpack", "price": 50, "details": "Durable and spacious backpack."},
        5: {"name": "Watch", "price": 150, "details": "Elegant wristwatch."},
    }

    while True:
        print("\nShopping Menu:")
        for key, item in menu.items():
            print(f"{key}. {item['name']} - ${item['price']}")

        choice = input("Enter the item number to view details, 'a' to add to cart, 'r' to remove from cart, '0' to exit: ").lower()

        if choice == '0':
            break
        elif choice == 'a':
            display_cart(shopping_cart)
            add_choice = int(input("Enter the item number to add to cart: "))
            if 1 <= add_choice <= len(menu):
                selected_item = menu[add_choice]
                add_to_cart(shopping_cart, selected_item)
            else:
                print("Invalid input. Please enter a valid item number.")
        elif choice == 'r':
            display_cart(shopping_cart)
            remove_choice = input("Enter the name of the item to remove from cart: ")
            remove_from_cart(shopping_cart, remove_choice)
        elif 1 <= int(choice) <= len(menu):
            selected_item = menu[int(choice)]
            print(f"\nDetails of {selected_item['name']}:\nPrice: ${selected_item['price']}\nDescription: {selected_item['details']}")
##            add_to_cart_response = input("Do you want to add this item to your cart? (yes/no): ").lower()
##            if add_to_cart_response == 'yes':
##                add_to_cart(shopping_cart, selected_item)
        else:
            print("Invalid input. Please enter a valid item number or 'a' to add to cart, 'r' to remove from cart, '0' to exit.")

    print("\nThank you for shopping with us!")
    display_cart(shopping_cart)
    print("\nCheckout - Total Bill:")
    total_bill = sum(item['price'] for item in shopping_cart)
    for item in shopping_cart:
        print(f"{item['name']} - ${item['price']}")
    print(f"Total: ${total_bill}")

cart_menu()
