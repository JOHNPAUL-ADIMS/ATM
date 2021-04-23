#GLOBAL
from datetime import time
from os import P_NOWAIT
import random
import time
from datetime import datetime
from getpass import getpass

import validation
import database


now = datetime.now()
currentDate = now.strftime("%d-%B-%Y")
currentTime = now.strftime("%I : %M %p")

userdatabasepath = "userRecord/"


def generateAccountNumber ():
    return random.randrange(1111111111,9999999999)


def initalization():
    print("Welcome to the BANK OF JP".center(10, '*').upper())
    print("""
        Do you have an account with us ?
            1. Yes
            2. No
    """)
    try:
        ownAccount = int(input("Enter your option>>>   "))
    except ValueError:
        return initalization()
    
    
    if (ownAccount == 1):
        return login()
    elif(ownAccount == 2):
        return registeration()
    else:
        print("You have selected invalid option")
        return initalization()


def login():
    print("***************Login to your new account***************")

    userAccountNumber = input("Enter your account number \n")
    isLoginNumberValidation = validation.loginNumberValidation(userAccountNumber)

    if isLoginNumberValidation:
        # password = input("Enter your password\n")
        password = getpass("Enter your password\n")

        user = database.authenticateUser(userAccountNumber, password)

        if user:
            print("Login successful\n\n")
            time.sleep(1.0)
            print(f'====WELCOME  to JP BANK '.upper())
            # importing date and time
            print("Today's date is == :", currentDate)
            print("Your time is ==", currentTime)
            print("********************************")
            print("********************************")
            
            return bankingOperation(userAccountNumber)

        else:
            print('\nInvalid account or password')
            return login()
    
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integer")
        return login()
    
   
    

def registeration():
    print('=== REGISTER BELOW ===')
    email = input("Enter your email address\t\n")
    firstName = input("Enter your first name\t\n")
    lastName = input("Enter your last name\t\n")
    password = getpass("Enter your password\n")

    accountNumber = generateAccountNumber()

    balance = 500
     
    isUserCreated = database.create(accountNumber, firstName, lastName, email, password, balance)

    if isUserCreated:
        print(f"{firstName}  Your account creation is successfull\n")
        print(" ====== ====== ====== ====== =====")
        print(f'Your account number is {accountNumber}\n')
        print("Keep your account number  safe ")
        
        login()

    else:
        print("Something went wrong, please try agian")
        registeration()


def bankingOperation(accountNumber):

    user = database.read(accountNumber)

    print(f"Welcome {user[0]} {user[1]}".title())
    print(""" What will you want to do 
        1. Deposit
        2. Withdrawal
        3. Complaint
        4. Balance
        5. Logout

    """)
  
    optionSelected =  int(input(">>  "))
    
   
    if(optionSelected == 1):
        return depositOperation(accountNumber)

    elif(optionSelected == 2):
        return withdrawalOperation(accountNumber)

    elif(optionSelected == 3):
        return complaintOperation (accountNumber)

    elif (optionSelected == 4):
        return getCurrentBalance(accountNumber)

    elif (optionSelected == 5):
        return logout(accountNumber)

    else:
        print("Invalid option selected")
        return bankingOperation(accountNumber)

 
def withdrawalOperation(accountNumber):

    action = 'withdraw'

    withdraw_amount = input("Enter Amount to Withdraw>\t#")

    is_valid = validation.validateInput(withdraw_amount)

    if not is_valid:
        return withdrawalOperation(accountNumber)

    else: 
        bal = database.update(accountNumber, action , withdraw_amount)
        
        if bal:
            print("Please take your cash.")

    return again(accountNumber)



def depositOperation(accountNumber):

    action = 'deposit'

    deposit_amount = input("Enter Amount to Deposit>\t#")

    is_valid = validation.validateInput(deposit_amount)

    if not is_valid:
        return depositOperation(accountNumber)

    else: 
        bal = database.update(accountNumber, action , deposit_amount)
        
        if bal:
            print("Deposit successful")

    return again(accountNumber)

    

def again(accountNumber):


    try:

        again = int(input("Do you want to perform another action?\n\t1. Yes\n\t2. No \n\n >"))

        if again == 1:
            return bankingOperation(accountNumber)

        elif again == 2:
             return logout(accountNumber)

        else:
            print("Invalid input")

    except ValueError:
        print("Enter 1 or 2.")
    return logout(user="")




def getCurrentBalance(accountNumber):

    balance = int(database.read(accountNumber)[-1])

    print(f"Your current balance is:\t #{balance}\n\n")

    return again(accountNumber)



def complaintOperation(accountNumber):
        print("What issue will you like to report")
        print("********************************")
        complaint = input("Enter your complaint\n")
            # database2 = [Complaint]  for 
        print(" Thank you for contacting us, your comment has been received by us")
        print("********************************")
        return again(accountNumber)


def logout(user):
    print(f'Do you want to exit?')
    print(f'If Yes press 1 or No press 2')
    try:
        exitoption = int(input('>>  '))
        time.sleep(0.5)
    except ValueError:
        print("You have made an invalid selection. Try again\n")
        return exit()
    try:

        if exitoption == 1:
            print("We will love to see you back")
            exit()

        elif exitoption == 2:
            return bankingOperation(user)
        else:
            return logout(user)
    except ValueError:
        print('Invalid Selection. Try again')
    return logout(user)



############### SYSTEM INITIALIZATION ###################
initalization()


