import sys

class FinanceSystem:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        print(f"Current Balance for {self.owner}: ${self.balance:.2f}")

    def show_history(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)
        print("-" * 20)

def main():
    name = input("Enter account owner name: ")
    account = FinanceSystem(name)
    
    while True:
        print("\n--- Finance System Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            account.show_history()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
import requests
import json

def fetch_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the response")
    return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    todo_item = fetch_api_data(api_url)

    if todo_item:
        print("Successfully fetched data:")
        print(json.dumps(todo_item, indent=2))
        print(f"\nTitle of the todo: {todo_item['title']}")
        print(f"Completed status: {todo_item['completed']}")