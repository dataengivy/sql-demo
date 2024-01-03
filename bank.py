import random
import json

class BankAccount():
    def __init__(self, load_from_file=True):
        self.accounts=self.load_accounts() if load_from_file else {}
    
    def load_accounts(self):
        try:
            with open("accounts.json","r")  as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def save_account(self):
        with open("accounts.json","w")  as f:
            json.dump(self.accounts,f)
    
    def close(self):
        self.save_account()

    def create_account(self):
        try:
            name = input("Enter your name: ")
            while True:
                phone = input("Enter your 10-digit phone number: ")
                if phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print("Invalid phone number. Please enter a valid 10-digit number.")
            account_number = random.randint(100000, 999999)
            while account_number in self.accounts:
                account_number = random.randint(100000, 999999)
            self.accounts[account_number]={"name":name,"phone":phone,"balance":0}
        except Exception as e:
            print(f"Error creating account: {e}")
    
    def close_account(self,account_number):
        try:
            if account_number in self.accounts:
                del self.accounts[account_number]
                print("Account with ID {account_number} has been deleted successfully.")
            else:
                print(f"Account not found!")
        except Exception as e:
            print(f"Error closing the account: {e}")
    
    def deposit(self,account_number,amount):
        try:
            if account_number in self.accounts:
                self.accounts[account_number]["balance"] += amount
                print(f"Amount {amount} deposited sucessfully!")
            else:
                print(f"Account number not found!")
        except Exception as e:
            print(f"Error deposit the amount: {e}")
    
    def withdrawl(self,account_number,amount):
        try:
            if account_number in self.accounts:
                if self.accounts[account_number]["balance"] >= amount:
                    self.accounts[account_number]["balance"] -= amount
                    print(f"Amount {amount} withdrawl sucessfully!")
                else:
                    print(f"Insufficient Balance!")
            else:
                print(f"Account number not found!")
        except Exception as e:
            print(f"Error withdrawl the amount: {e}")

def main():
    bank=BankAccount()
    while True:
        print("\n Bank Management System")
        print("1. Create Account")
        print("2. Close Account")
        print("3. Deposit Money")
        print("4. Withdrawl Money")
        print("5. Exit")

        choice=input("Enter your choice")
        if choice =="1":
            bank.create_account()
        elif choice == "2":
            account_number=input("Enter your Bank account number: ")
            bank.close_account(account_number)
        elif choice == "3":
            account_number=input("Enter your Bank account number: ")
            amount=input("Enter the deposit amount: ")
            bank.deposit(account_number,amount)
        elif choice == "4":
            account_number=input("Enter your Bank account number: ")
            amount=input("Enter the deposit amount: ")
            bank.withdrawl(account_number,amount)
        elif choice == "5":
            bank.close()
            break
        else:
            print("Invalid coice, choose correct one")

if __name__ == "__main__":
    main()