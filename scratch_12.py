#2. When the user selects option 1, they should be presented with the following:
#- How much would you like to withdraw (receive input from the user), output "take your cash"
#3. When the user selects option 2, present them with the following options:
#- How much would you like to deposit? (receive input from the user), output current balance.
#4. When the user selects complaint, present them with the following options:
#- What issue will you like to report? (Receive input from the user), output "Thank you for contacting us"
#5. Account number generation
#6. Register and login
#7. Any other improvement


# Create Account... (user email, User first name, user password ,Account number generation)
# Login and logout... (Login with Account number and password)
# Bank Operations... (Withdraw, Transfer, Check account Balance, Customer Care[What is my Account number, forgotten password])]'



import random
accounts = {}

def homepage():
    print('Welcome to Zuri Bank, please how may we be of help')
    choice = input('''1. I want to create an account
    2. Login
    3. Customer care
    ''')
    if choice == '1':
        create_account()
    elif choice == '2':
        login()
    elif choice == '3':
        customer_care()
    else:
        homepage()

def customer_care():
    print('Welcome to Zuri Bank customer customer care line, please how may we be of help to you?')
    choose = input('1. I have a complaint\n2. Forgotten Password\n 3. Forgotten Account Number\n:')
    if choose == '1':
        input('What is your complaint?\n:')
        print('Thank you for letting us know your banking issue, we will get bank to you soonest!')
    elif choose == '2':
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        email = input('Enter your email address: ')
        account_numb = int(input('Enter your account number: '))
        if account_numb in accounts:
            accounts_cred = list(accounts[account_numb][0:3])
            # entered_cred = (first_name, last_name, email)
            # print(accounts_cred)
            # print(entered_cred)
            if [first_name, last_name, email] == accounts_cred:
                print(
                    'A reset link has been sent to your email, kindly visit any of our offline branches to activate the link and reset your password')
            else:
                print('Wrong credentials')
                customer_care()
        else:
            print('Your record does not exist')
    elif choose == '3':
        first_name = input('Enter your first name: ')
        last_name = input('Enter your last name: ')
        email = input('Enter your email address: ')
        password = input('Enter your account password: ')
        entered_cred = [first_name, last_name, email, password]

        def get_key(val):
            for key, value in accounts.items():
                if entered_cred == value[0:4]:
                    # return key
                    print(f'This is your account number {key}')
            print(
                'The credentials you entered are wrong, please visit our offline branches to rectify your issue\n')

            customer_care()

        get_key(entered_cred)


def create_account():
    first_name = input('please enter your first name: ')
    last_name = input('please enter your last name: ')
    email = input('please enter your email')
    password = input('please create your password')
    account_num = int(random.randrange(1111111111, 9999999999))
    account_balance = int(random.randrange(1111111111, 9999999999))
    print(f'Welcome to Bank Zuri, {first_name}. This is your account number {account_num}')
    accounts.update({account_num: [first_name, last_name, email, password, account_balance]})
    print(accounts)
    login()

def login():

    def bank_ops():
        print('What would you like to do?')
        choose = input("1. Make Withdrawal \n2. Make Deposit \n3. Make Transfer \n4. Check Account Balance \n5. Customer Care \n:")
        if choose == '1':
            withdraw()
        elif choose == '2':
            deposit()
        elif choose == '3':
            transfer()
        elif choose == '4':
            check_balance()
        elif choose == '5':
            customer_care()
        else:
            bank_ops()


    def withdraw():
        account_balance = accounts[account_num][4]
        to_withdraw = int(input('How much do you want to withdraw:\n'))
        if to_withdraw < account_balance:
            print('Take your cash')
            #print(accounts[account_num][4])
            accounts[account_num][4] = accounts[account_num][4] - to_withdraw
            new_balance = accounts[account_num][4]
            print(f'Your new balance is {new_balance}btc')
            print('If you want to perform another transaction press 1: ')
            print('Or press 0 to exit')
            user_choice = input(': ')
            if user_choice == '1':
                bank_ops()
            else:
                print('Thanks for banking with us')

        else:
            print('insufficient funds')


    def deposit():
        to_deposit = int(input('How much do you want to deposit:\n'))
        accounts[account_num][4] = accounts[account_num][4] + to_deposit
        new_balance = accounts[account_num][4] = to_deposit
        print(f'Your new balance is {new_balance}btc')
        print('If you want to perform another transaction press 1: ')
        print('Or press 0 to exit')
        user_choice = input(': ')
        if user_choice == '1':
            bank_ops()
        else:
            print('Thanks for banking with us')

    def transfer():
        account_balance = accounts[account_num][4]
        to_transfer = int(input('How much do you want to transfer: '))
        transfer_receiver = int(input('enter the recipient\'s account number:\n'))
        if transfer_receiver > 1000000000 < 9999999999 and to_transfer < account_balance:
            print('Your transfer was successful')
            print(f'This is your new account balance {account_balance - to_transfer}btc')
            print('If you want to perform another transaction press 1: ')
            print('Or press 0 to exit')
            user_choice = input(': ')
            if user_choice == '1':
                bank_ops()
            else:
                print('Thanks for banking with us')
        else:
            print(f'The account {transfer_receiver} does not exist')
            print('If you want to perform another transaction press 1: ')
            print('Or press 0 to exit')
            user_choice = input(': ')
            if user_choice == '1':
                bank_ops()
            else:
                print('Thanks for banking with us')

    def check_balance():

        print(f'Your account balance is {accounts[account_num][4]}btc')
        print('If you want to perform another transaction press 1: ')
        print('Or press 0 to exit')
        user_choice = input(': ')
        if user_choice == '1':
            bank_ops()
        else:
            print('Thanks for banking with us')

    def customer_care():
        print('Welcome to Zuri Bank customer customer care line, please how may we be of help to you?')
        choose = input('1. I have a complaint\n2. Forgotten Password\n 3. Forgotten Account Number\n:')
        if choose == '1':
            input('What is your complaint?\n:')
            print('Thank you for letting us know your banking issue, we will get bank to you soonest!')
        elif choose == '2':
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            email = input('Enter your email address: ')
            account_numb = int(input('Enter your account number: '))
            if account_numb in accounts:
                accounts_cred = list(accounts[account_numb][0:3])
                #entered_cred = (first_name, last_name, email)
                #print(accounts_cred)
                #print(entered_cred)
                if [first_name, last_name, email] ==  accounts_cred:
                    print('A reset link has been sent to your email, kindly visit any of our offline branches to activate the link and reset your password')
                else:
                    print('Wrong credentials')
                    customer_care()
            else:
                print('Your record does not exist')
        elif choose == '3':
            first_name = input('Enter your first name: ')
            last_name = input('Enter your last name: ')
            email = input('Enter your email address: ')
            password = input('Enter your account password: ')
            entered_cred = [first_name, last_name, email, password]
            def get_key(val):
                for key, value in accounts.items():
                    if entered_cred == value[0:4]:
                        #return key
                        print(f'This is your account number {key}')
                        login()
                    else:
                        print('The credentials you entered are wrong, please visit our offline branches to rectify your issue\n')
                        customer_care()
            get_key(entered_cred)
    print('Welcome to Zuri bank!')
    account_num = int(input('enter your account number: '))
    #print(accounts)
    if account_num in accounts:
        password = accounts[account_num][3]
        password_attempt = input('enter your password: ')
        if password_attempt == password:
            print(f'Welcome back {accounts[account_num][0]} {accounts[account_num][1]}')
            bank_ops()
        else:
            print('Wrong Password!')
            choice = input('''What would you like to do?
                    1. Create Account
                    2. Try Again
                    3. Exit
                    : ''')
            if choice == '1':
                create_account()
            elif choice == '2':
                login()
            elif choice == '3':
                print('Thanks for Banking with us. Do have a nice day!')
                homepage()
            else:
                print('wrong input')
    else:
        print('Account not found')
        choice = input('''What would you like to do?
        1. Create Account
        2. Try Again
        3. Exit
        : ''')
        if choice == '1':
           create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print('Thanks for Banking with us. Do have a nice day!')



homepage()