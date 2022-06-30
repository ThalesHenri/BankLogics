from account import Account
class VipAccount(Account):
    def __init__(self, name, cpf, password):
        super().__init__(name,cpf, password)
        self.balance = 2000



