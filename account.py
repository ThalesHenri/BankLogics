class Account:
    def __init__(self,  name, cpf, password):
        self.name = name
        self.cpf = cpf
        self.balance = 0.0
        self.extract = []
        self.password = password

    def deposit(self, amount):
        float(amount)
        self.balance += amount  #incrementation
        print('Mr.{},Your balance has been updated to $ {}'.format(self.name, self.balance))
        e = ("A deposit in the ammount of {} was made.".format(amount))
        self.extract.append(e)
        return self.balance, self.extract

    def show_balance(self):
        print('Your account actual balance is ${}'.format(self.balance))

    def withdraw(self, amount):
        if self.balance < amount:  #validation of funds
            print('Insuficient funds to make that operation!')
        else :
            self.balance = self.balance - amount
            print('Mr.{} Your balance has been updated to $ {}'.format(self.name, self.balance))
            e = ("A withdraw in the ammount of {} was made.".format(amount))
            self.extract.append(e)
            return self.balance, self.extract

    def show_extract(self):
        if not self.extract:
            print('Your extract is empty')
        else:
            for c in self.extract:
                print(c)






