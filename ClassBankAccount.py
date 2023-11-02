from Bank import bankAccount

class SavingsAccount(bankAccount):
    def __init__(self, account_number, interest_rate, balance = 0):
        super().__init__(account_number, balance)
        self.iterest_rate = 5

    def interest_generated(self, months):
        interest = self.balance * self.interest_rate / 100 * months
        return interest

savings_account = bankAccount("ES1111111111111111111", 6)
checking_account = bankAccount("ES2222222222222222222",)