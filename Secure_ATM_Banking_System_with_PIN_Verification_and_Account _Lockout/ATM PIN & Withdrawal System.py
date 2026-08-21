#task: PIN Verification user should be given 3 chances if 3rd chance is over
#it should return Account Locked for 24hours -->balance, hithdrawl,show the number of chances you have

correct_pin = "1801"
attempts = 3
balance = 20000

while attempts > 0:
    pin = input("Enter your ATM PIN: ")

    if pin == correct_pin:
        print("Login Successful")

        choice = ""

        while choice != "3":
            print("\nATM MENU")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your Balance is:", balance)

            else:
                if choice == "2":
                    amount = int(input("Enter amount to withdraw: "))

                    if amount <= balance:
                        balance = balance - amount
                        print("Withdrawal Successful")
                        print("Remaining Balance:", balance)
                    else:
                        print("Insufficient Balance")

                else:
                    if choice == "3":
                        print("Thank you for using our ATM.")
                    else:
                        print("Invalid Choice")

        break

    else:
        attempts = attempts - 1

        if attempts > 0:
            print("Incorrect PIN")
            print("You have", attempts, "chance(s) left.")
        else:
            print("Account Locked for 24 hours.")
            print("You have used all 3 attempts.")











            
