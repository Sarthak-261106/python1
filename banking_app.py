print("======================")
print('Welcome to Banking App')
print("======================")


def check_balance():
    print('checking balance')
    global balance
    print(f"your current balance is {balance}")
    print("======================")
    return balance

def deposit(amount):
    global balance
    print("depositing")
    if amount > 0:
        balance = balance + amount
        print(f"Amount added and your account new balance is {check_balance()}")
        print("======================")
    else:
        print("Deposit failed")


def withdraw(amount):
    print('withdrawing')
    global balance
    if amount<=0:
        print('cannot withdraw 0 or negative amount')
        print("======================")
    elif amount>balance:
        print("not enough balance")
        print("======================")
    else:
     balance=balance-amount
     print(f'amount removed and your account new balance is {check_balance()} ')
     print("======================")


balance=0


while True:
    print('1.to check balance')
    print('2.to deposit')
    print('3.to withdraw')
    print('4.exit')
    choice=(input('Enter your choice:'))
    print("======================")


    if choice=='1':
        check_balance()
    elif choice=='2':
        amount = float(input('how much do you want to deposit?'))
        deposit(amount)
    elif choice=='3':
        amount = float(input('how much do you want to withdraw?'))
        withdraw(amount)
    elif choice=='4':
        break
    else:
        print('Enter a valid choice')

print('Thank you for using this application')
