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

        choice = int(input("Enter the item number to view details (0 to exit): "))

        if choice == 0:
            break
        elif 1 <= choice <= len(menu):
            selected_item = menu[choice]
            print(f"\nDetails of {selected_item['name']}:\nPrice: ${selected_item['price']}\nDescription: {selected_item['details']}")

            add_to_cart_response = input("Do you want to add this item to your cart? (yes/no): ").lower()
            if add_to_cart_response == 'yes':
                shopping_cart.append(selected_item)
                print(f"{selected_item['name']} added to the cart.")
        else:
            print("Invalid input. Please enter a valid item number.")

    print("\nThank you for shopping with us!")
    if shopping_cart:
        print("Items in your cart:")
        for item in shopping_cart:
            print(f"{item['name']} - ${item['price']}")
    print("\nCheckout - Total Bill:")
    total_bill = sum(item['price'] for item in shopping_cart)
    for item in shopping_cart:
        print(f"{item['name']} - ${item['price']}")
    print(f"Total: ${total_bill}")


cart_menu()
