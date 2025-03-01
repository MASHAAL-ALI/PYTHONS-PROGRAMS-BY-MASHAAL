def main():
    shopping_cart = []
    menu = {
        1: {"name": "Laptop", "price": 1000},
        2: {"name": "Headphones", "price": 100},
        3: {"name": "Smartphone", "price": 500},
        4: {"name": "Backpack", "price": 50},
        5: {"name": "Watch", "price": 150},
    }

    while True:
        print("\nShopping Menu:")
        for key, item in menu.items():
            print(f"{key}. {item['name']} - ${item['price']}")

        choice = int(input("Enter the item number to add to cart (0 to checkout): "))

        if choice == 0:
            break
        elif 1 <= choice <= len(menu):
            selected_item = menu[choice]
            shopping_cart.append(selected_item)
            print(f"{selected_item['name']} added to the cart.")
        else:
            print("Invalid input. Please enter a valid item number.")

    print("\nCheckout - Total Bill:")
    total_bill = sum(item['price'] for item in shopping_cart)
    for item in shopping_cart:
        print(f"{item['name']} - ${item['price']}")
    print(f"Total: ${total_bill}")


main()
