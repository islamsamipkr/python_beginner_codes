# Starting bank balance
balance = 1000

# Keep the ATM running
while True:

    # Display the ATM menu
    print("\n--- Python Bank ATM ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Ask the user what they want to do
    choice = input("Choose an option: ")

    # OPTION 1: Check balance
    if choice == "1":

        # Display the current balance
        print("Your balance is $", balance)

    # OPTION 2: Deposit money
    elif choice == "2":

        # Ask how much money they want to deposit
        deposit = float(input("How much would you like to deposit? $"))

        # Add the deposit to the existing balance
        balance = balance + deposit

        # Show the new balance
        print("Deposit successful!")
        print("New balance: $", balance)

    # OPTION 3: Withdraw money
    elif choice == "3":

        # Ask how much money they want
        withdrawal = float(input("How much would you like to withdraw? $"))

        # Check whether the account has enough money
        if withdrawal <= balance:

            # Subtract the withdrawal from the balance
            balance = balance - withdrawal

            # Tell the customer it worked
            print("Please take your cash. 💵")

            # Show the remaining balance
            print("Remaining balance: $", balance)

        else:

            # This happens when there isn't enough money
            print("Insufficient funds!")

    # OPTION 4: Exit
    elif choice == "4":

        # Say goodbye
        print("Thank you for using Python Bank!")

        # Break ends the while loop
        break

    # Handle an incorrect menu choice
    else:

        # Tell the user to choose again
        print("Invalid option. Please choose 1, 2, 3, or 4.")
