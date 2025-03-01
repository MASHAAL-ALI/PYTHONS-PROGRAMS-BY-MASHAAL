def add_to_cart(cart, item):
    cart.append(item)
    print(f"{item['name']} added to the cart.")

def view_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item in cart:
            print(f"{item['name']} - {item['price']}")

def generate_shopping_menu():
    menu = {
        1: {"name": "Laptop", "price": 1000, "details": "High-performance laptop."},
        2: {"name": "Headphones", "price": 100, "details": "Noise-canceling headphones."},
        3: {"name": "Smartphone", "price": 500, "details": "Latest smartphone model."},
        4: {"name": "Backpack", "price": 50, "details": "Durable and spacious backpack."},
        5: {"name": "Watch", "price": 150, "details": "Elegant wristwatch."},
    }
    return menu

def display_menu(menu):
    print("Shopping Menu:")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ${item['price']}")

def main():
    shopping_cart = []

    menu = generate_shopping_menu()

    while True:
        display_menu(menu)

        choice = int(input("Enter the item number to view details (0 to exit): "))
        if choice == 0:
            break
        elif choice and 1 <= choice <= len(menu):
            selected_item = menu[choice]
            print(f"\nDetails of {selected_item['name']}:")
            print(f"Price: ${selected_item['price']}")
            print(f"Description: {selected_item['details']}")
            
            add_to_cart_response = input("Do you want to add this item to your cart? (yes/no): ").lower()
            if add_to_cart_response == 'yes':
                add_to_cart(shopping_cart, selected_item)
        else:
            print("Invalid input. Please enter a valid item number.")

    print("\nThank you for shopping with us!")
    view_cart(shopping_cart)


main()