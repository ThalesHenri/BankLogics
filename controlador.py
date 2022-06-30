# Banco do th, welcome my friend !
from bank import Bank

class Controlador:
    def __init__(self):
        pass


thbank = Bank()  #Bank's object
print('=+' * 20)
print('Welcome to the TH Bank')
print('First you need to create an account: ')
t = int(input('Choose the type of your account\n1 - Normal Account\n2 - Vip Account\n'))
if t == 1:
    print('Type your personal data')
    a = input('NAME > ')
    b = input('CPF > ')
    c = input('PASSWORD > ')
    thbank.create_account(a, b, c)

elif t == 2:
    print('Type your personal data')
    x = input('NAME >')
    y = input('CPF > ')
    z = input('PASSWORD >')
    thbank.create_vip_account(x, y, z)

while True:
    print('=+' * 20)
    print('Choose what you want to do ')
    print('1 - Deposit\n2 - Withdraw\n3 - Create another Account\n4 - Show account balance\n5 - Login account\n'
          '6 - Save Accountlist\n7 - Make a loan\n8 - Exit\n9 - Extract')

    print('=+' * 20)
    a = int(input(''))
    if a == 1:
        c = float(input(' Type the amount that you want to deposit > $'))
        thbank.make_deposit(c)

    elif a == 2:  #withdraw
        c = float(input('Type the amount that you want to withdraw > $ '))
        thbank.make_withdraw(c)

    elif a == 3:  # create another acount
        t = int(input('Choose the type of your account\n1 - Normal Account\n2 - Vip Account\n'))
        if t == 1:
            print('Type your personal data')
            a = input('NAME >')
            b = input('CPF > ')
            c = input('PASSWORD > ')
            thbank.create_account(a, b, c)
        elif t == 2:
            print('Type your personal data')
            x = input('NAME >')
            y = input('CPF > ')
            z = input('PASSWORD > ')
            thbank.create_vip_account(x, y, z)

    elif a == 4:  # show balance
        thbank.show_account_balance()

    elif a == 5:  #login
        print('#' * 20)
        print ('Type your personal data.')
        n = input('Name > ')
        p = input('Password > ')
        thbank.login(n , p)


    elif a == 6:  #save accountlist
        thbank.save_created_accounts()

    elif a == 7:  #loan function with a predeterminated fund (needtofix)
        thbank.loan()

    elif a == 8:
        break
        print('Exiting the program! ')

    elif a == 9:
        thbank.see_extract()
