class Account:
    def __init__ (self, username, password, balance):
        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, new balance: {self.balance}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

class Atm:
    def __init__(self):
        self.accounts = {
            'Alice': Account('Alice', 'password123', 1000),
            'Bob': Account('Bob', 'password456', 500),
            'Charlie': Account('Charlie', 'password789', 2000)
        }
        self.current_user = None

    def login(self):
        login_attempt = 3
        while login_attempt > 0:
            username = input("Enter username: ")
            password = input("Enter password: ")
            account = self.accounts.get(username)

            if account and account.password == password:
                self.current_user = account
                print(f"Welcome, {username}!")
                self.menu()
            else:
                login_attempt -= 1
                print(f"Invalid credentials. You have {login_attempt} attempts left.")
                if login_attempt == 0:
                    print("Too many failed attempts. Exiting.")
                    exit()

    def menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                self.current_user.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.current_user.withdraw(amount)
            elif choice == '3':
                self.current_user.check_balance()
            elif choice == '4':
                print("Logging out...")
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

atm = Atm()
atm.login()