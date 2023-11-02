class bankAccount:
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
    def get_account_number(self):
        return self.account_number

    def add_funds(self, funds):
        self.balance = self.balance + funds

    def retire_funds(self, funds):
        self.balance = self.balance - funds

    def get_balance(self):
        return self.balance

bank_account1 = bankAccount("ES000000000000000000000000000")

bank_account1.add_funds(float(100))
bank_account1.retire_funds(float(38))


print(f"La cuenta con número: {bankAccount} tiene {bankAccount.get_balance()}€ en su balance")