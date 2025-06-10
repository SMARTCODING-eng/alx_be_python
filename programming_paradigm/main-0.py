import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands:")
        print("deposit:<amount>  - Add money to account")
        print("withdraw:<amount> - Take money from account")
        print("display           - Show current balance")
        print("\nExample:python main.py deposit:50")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)


    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()