# Banking System

# List to store account numbers
account_numbers = [1001, 1002, 1003]

# Dictionary to store customer details
customers = {
    1001: {"name": "Jasmeen", "balance": 5000},
    1002: {"name": "Aman", "balance": 7000},
    1003: {"name": "Simran", "balance": 10000}
}

# Bank Account Class
class BankAccount:
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    # Deposit Function
    def deposit(self, amount):
        self.balance += amount
        self.save_transaction(f"Deposited ₹{amount}")
        print("Amount deposited successfully.")

    # Withdraw Function
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient Balance")

            self.balance -= amount
            self.save_transaction(f"Withdrawn ₹{amount}")
            print("Withdrawal successful.")

        except ValueError as e:
            print("Error:", e)

    # Balance Inquiry
    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    # Save Transaction to File
    def save_transaction(self, transaction):
        with open("Banking system/transactions.txt", "a") as file:
            file.write(
                f"Account No: {self.acc_no}, "
                f"Name: {self.name}, "
                f"{transaction}, "
                f"Balance: ₹{self.balance}\n"
            )


# Main Program
while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Inquiry")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "4":
        print("Thank You!")
        break

    acc_no = int(input("Enter Account Number: "))

    if acc_no not in account_numbers:
        print("Account not found!")
        continue

    account = BankAccount(
        acc_no,
        customers[acc_no]["name"],
        customers[acc_no]["balance"]
    )

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    else:
        print("Invalid Choice!")

    # Update dictionary balance
    customers[acc_no]["balance"] = account.balance