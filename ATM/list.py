

accounts = {
    "Arti": {"pin": "1111", "balance": 50000},
    "Sneha": {"pin": "2222", "balance": 60000},
    "Neelam": {"pin": "3333", "balance": 70000},
    "Shivani": {"pin": "4444", "balance": 80000}
}

def atm():
    name = input("Enter account name: ")

    if name not in accounts:
        print("Account not found!")
        return

    pin = input("Enter PIN: ")

    if pin != accounts[name]["pin"]:
        print("Incorrect PIN!")
        return

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            print("Balance:", accounts[name]["balance"])

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            accounts[name]["balance"] += amount
            print("Deposited successfully!")

        elif choice == "3":
            amount = float(input("Enter withdraw amount: "))
            if amount <= accounts[name]["balance"]:
                accounts[name]["balance"] -= amount
                print("Withdrawn successfully!")
            else:
                print("Insufficient balance!")

        elif choice == "4":
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid choice!")
atm()
