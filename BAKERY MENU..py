print("""
Welcome to cakeshake!!
we offer you the following saviours:
 1.cake(price:650/-)
 2.cookie jars(price:240\-)
 3.sandwiches(price:100\-)

""")
choice=int(input("Enter your choice number: "))
if choice == 1:
    quantity=int(input("How many cakes?"))
    bill_cake=quantity*650
    print("Your total bill is Rs." ,bill_cake)
    print("Your order will be delivered in 30 minutes")
elif choice==2:
    quantity=int(input("How many cookie jars?"))
    bill_cookie=quantity*240
    print("Your total bill is Rs." ,bill_cookie)
    print("Your order will be delivered in 30 minutes")
elif choice==3:
    quantity=int(input("How many sandwiches?"))
    print("Your total bill is Rs." ,bill_sandwiches)
    print("Your order will be delivered in 30 minutes")
else:
    print("The choice number you entered is not valid")
print("Thank you for visiting!!")
    
    
