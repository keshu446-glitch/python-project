def atm_machin():
    while True:
        print("welcome to the atm machine:")
        balance=10000
        pin=1234
        withdrawal_count=5000
        while true:
            print("choose an option:")
            print("1. check balance")
            print("2.deposite")
            print("3.withdraw money")
            print("4.exit")
            choice=input("enter your choice(1-4):")
            if choice=='1':
                print (" your current balance is: {balance}")
            elif choice=='2':
                print("pin")
                deposite=float(input(" enter amount to deposite:"))
                if deposite>0:
                    balance+=deposite
                    print("{deposit:} deposit sucessfully!")
                elif  ValueError:
                    print("invalid input . please enter a numeric value. ")
                elif choice =='3':
                    print
                    withdraw= float (input("enter amount to withdraw:"))
                    if withdraw >0:
                        if withdraw <=balance:
                            balance-=withdrawal
                            print("{withdraw:}withdraw succesfully!")
                        else:
                            print("insufficient balance.")
                    else:
                        print (" invalid amount .please enter a positive number.")
                    exept  
                    print(" invalid input. please enter a numeric value.")
                elif choice=='4':
                    print(" thankyou for using the ATM. good bye!")
                    break
                else:
                    print (" invalid cjoice. try again!")
    print(atm_machin())
