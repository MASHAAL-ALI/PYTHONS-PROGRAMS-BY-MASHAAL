balance=10000
account_id=int(input("ENTER YOUR ID: "))
while True:
    print("""
MAIN MENU
**************
1.Deposit Money
2.Withdraw Amount
3.Login as Different User""")
    choice=int(input('Select Your Choice....: '))
    if choice==1:
        amount=int(input('Enter Amount: '))
        balance+=amount
        question=input("Do you want to continue: ")
        if question!="Y" and question!="y":
            break
    elif choice==2:
        amount=int(input('Enter Amount: '))
        balance-=amount
        input("Do you want to continue: ")
        if question!="Y" and question!='y':
            break
    elif choice==3:
        break
    else:
        print("choice not valid")
        break
    
