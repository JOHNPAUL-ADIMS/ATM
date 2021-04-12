#GLOBAL 

from datetime import time
from os import P_NOWAIT
from babel import numbers
import random
import time
from datetime import datetime
now = datetime.now()
currentDate = now.strftime("%d-%B-%Y")
currentTime = now.strftime("%I : %M %p")
database = {}
database2 = {}

#  TO DO LIST BY TOMORROW
# 1. Remember to change the dictionary to google sheet
# 2. Remember to work on how to save the complaints on google sheet



def generateAccountNumber ():
    return random.randrange(1111111111,9999999999)


def initalization():
    print("Welcome to the BANK OF JP".center(10, '*').upper())
    print("""
        Do you have an account with us ?
            1. Yes
            2. No
    """)
    
    ownAccount = int(input("Enter your option>>>   "))
    
    try:
        if (ownAccount == 1):
            login()
        elif(ownAccount == 2):
            print(registeration())
        else:
            print("You have selected invalid option")
    except ValueError:
        print('Invalid option: Try again later')
        return initalization()

    initalization()


def registeration():
    print('=== REGISTER BELOW ===')

    try:
        email = input("Enter your email address\t\n")
        firstName = input("Enter your first name\t\n")
        lastName = input("Enter your last name\t\n")
        password = input ("Create a password\t\n")

    except NameError:
        print('Invalid option: Try again later')
        return registeration()

    accountNumber = generateAccountNumber()

    database[accountNumber] = [firstName, lastName, email, password]
    
    print(f"{firstName}  Your account creation is successfull")
    print(" ====== ====== ====== ====== =====")
    print(f'  Your account number is {accountNumber}')
    print("Make your account number is safe ")

    login()

def login():
    print("***************Login to your new account***************")
    userAccountNumber = int(input("Enter your account number \n"))
    isLoginNumberValidation = loginNumberValidation(userAccountNumber)

    if isLoginNumberValidation:
        password = input("Enter your password\n")

        for accountNumber, userDetails in database.items():
            if (userAccountNumber == accountNumber):
                if(userDetails[3] == password):
                    
                    print(f'==== WELCOME {userDetails[0]} to JP BANK ')
                # importing date and time
                    print("Today's date is == :", currentDate)
                    print("Your time is ==", currentTime)
                    print("********************************")
                    print("********************************")
                    bankingOperation(userDetails)
                else:
                    print("Invalid account or password, Enter your correct account Number")
                    login()
            # print('Invalid account or password')
            else:
                login()
    else:
        login()



def loginNumberValidation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:

            try:
                int(accountNumber)
            except ValueError:
                print("Invalid Account Number, account number should be an integer")
                return False
            except TypeError:
                print ("Invalid Account Number")
    else:
        print("Account Number is a required filled")
        return False


def bankingOperation(user):
    print(f"Welcome {user[0]}")
    print(""" What will you want to do 
        1. Deposit
        2. Withdrawal
        3. Complaint
        4. Logout

    """)
    try:
        optionSelected =  int(input(">>  "))
    except ValueError:
        print('Invalid option: Try again later')
        return bankingOperation()
    try:
        if(optionSelected == 1):
            depositOperation()
        elif(optionSelected == 2):
            withdrawalOperation()
        elif(optionSelected == 3):
            complaintOperation ()
        elif (optionSelected == 4):
            logout()
        else:
            print("Invalid option selected")
            bankingOperation(user)

    except ValueError:
        print('Invalid option: Try again later')
        return bankingOperation()
    return bankingOperation()

def withdrawalOperation(user):
    print("How much would you like to withdraw?\n")
    print("********************************")

    try:
        withdraw = float(input("Enter your amount\t "))
        print("********************************")
        print("Take your cash, %d" %withdraw)

    except ValueError:
        print('Invalid option: Try again later')
        return withdrawalOperation(user)
    return bankingOperation(user)

def depositOperation(user):       
    print("How much will you like to deposit?\n")
    print("********************************")

    try:
        deposit = float(input("Enter your current deposit\n"))
        print("Your Current Balance is %d " %deposit)
        print("********************************")
    except ValueError:
        print('Invalid option: Try again later')
        return depositOperation(user)
    return bankingOperation(user)

def complaintOperation(user):
    print("What issue will you like to report")
    print("********************************")
    complaint = input("Enter your complaint\n")
        # database2 = [Complaint]  for 
    print(" Thank you for contacting us")
    print("********************************")
    return bankingOperation(user)


def logout():
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
            return bankingOperation()
        else:
            return logout()
    except ValueError:
        print('Invalid Selection. Try again')
    return logout()



############### SYSTEM INITIALIZATION ###################
initalization()
