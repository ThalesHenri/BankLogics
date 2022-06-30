"""this is the bank, is his does basicaly all the functions manipuled by the controller class"""
from account import Account
from vip import VipAccount

class Bank:
    def __init__(self):
        self.loan_balance = 10000
        self.tool = []
# bank's functions
    
    def create_vip_account(self, x, y, z):
        self.account1 = VipAccount(x, y, z)
        self.tool.append(self.account1)
        print('Your V.I.P. account has been created')

    def create_account(self, x, y, z):
        self.account1 = Account(x, y, z)
        self.tool.append(self.account1)
        print('Your account has been created')
        return self.tool

    def save_created_accounts(self):
        with open('accounts.txt', 'a') as file:
            file.write('{}'.format(self.tool))
        print('Your accountlist has been saved!')

    def loan(self):  #  need to fix
        value = float(input('Type the value that you want to loan from our bank!\n'
                            ' We have a ${} fund for loan '.format(self.loan_balance)))
        if self.loan_balance < value:
            print('Insuficient Bank funds')
        else :
            self.account1.balance += value
            print('Your account balance has been updated for {} '.format(self.account1.balance))
        return self.loan_balance

    ''' in that case also as with the withdraw function, the class bank and account has conections between thenself'''
    
    def make_deposit(self,c):
        self.account1.deposit(c)

    def show_account_balance(self):
        self.account1.show_balance()


    def make_withdraw(self,c):
        self.account1.withdraw(c)

    def login(self, n, p):
        acess = False
        for c in self.tool:
            if (n == c.name and p == c.password):
                acess = True
                print('Hello MR {}.'.format(c.name))
                self.account1 = c
                return self.account1

        if acess == False:
            print('Wrong login or password information.')


    def see_extract(self):
        self.account1.show_extract()







