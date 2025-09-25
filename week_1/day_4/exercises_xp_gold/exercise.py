class BankAccount():
    def __init__(self, balance, user_name, password):
        self.balance = balance
        self.user_name = user_name
        self.password = password
        self.authenticated = False
    
    
    def authenticate(self):
        user_name = input("enter user_name: ")
        password = input("enter password: ")

        if user_name == self.user_name and password == self.password:
            self.authenticated = True

        else:
            print("user_name or password is incorrect!!!")

    def deposit(self, deposit_amount):
        if self.authenticated:
            try:
                int(deposit_amount)
                if deposit_amount > 0:
                    self.balance += deposit_amount
                else:
                    print("Invalid amount")
            except:
                print("Invalid input")
            '''
            if int(deposit_amount) < 0:
                raise ValueError("Invalid amount")
            self.balance += deposit_amount
            '''

        else:
            print("you can't access")


    def withdraw(self, withdraw_amount):
            
            if self.authenticated :
                try:
                    int(withdraw_amount)
                    if withdraw_amount > 0:
                        self.balance -= withdraw_amount
                    else:
                        print("Invalid amount")

                except:
                    print("Invalid input")
                '''
                if int(withdraw_amount) > 0:
                    self.balance -= withdraw_amount

                else:
                    print("Invalid amount")
                '''
            else:
                print("you can't access")
    
    def show_balance(self):
        if self.authenticated:
            print(self.balance)
    
class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance, user_name, password):
        super().__init__(balance, user_name, password)
        self.minimum_balance = 0

    def withdraw(self, withdraw_amount):
        
        if self.balance - withdraw_amount < self.minimum_balance:
            print("you can't withdraw this amount")
        else:
            super().withdraw(withdraw_amount)

my_account = MinimumBalanceAccount(1000, "person", "130030")
my_account.authenticate()
my_account.deposit(300)
my_account.withdraw(1000)
my_account.show_balance()