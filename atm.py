balance = 5000
while True:
    print("Your balance is: $" + str(balance))
    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter you choice (1, 2, or 3): ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print("Deposited $" + str(amount) + ". New balance is: $" + str(balance))
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds. Your balance is: $" + str(balance))
        else:
            balance -= amount
            print("Withdrew $" + str(amount) + ". New balance is: $" + str(balance))
    elif choice == "3": 
        print("Exiting. Your final balance is: $" + str(balance))
        break
    else:
        print("Invalid choice. Please try again.") 
      
      