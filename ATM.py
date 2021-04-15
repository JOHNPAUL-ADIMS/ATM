#GLOBAL
from datetime import time
from os import P_NOWAIT
import random
import time
from datetime import datetime
import validation
import database
from getpass import getpass
now = datetime.now()
currentDate = now.strftime("%d-%B-%Y")
currentTime = now.strftime("%I : %M %p")



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
        login()
    elif(ownAccount == 2):
        registeration()
    else:
        print("You have selected invalid option")
        initalization()


def login():
    print("***************Login to your new account***************")
    try:    
        userAccountNumber = input("Enter your account number \n")
        isLoginNumberValidation = validation.loginNumberValidation(userAccountNumber)
    except ValueError:
        return login()
    try: 
        if isLoginNumberValidation:
            # password = input("Enter your password\n")
            password = getpass("Enter your password\n")

            user = database.authenticateUser(userAccountNumber, password)

            if user:
                print("Login successfull\n\n")
                time.sleep(1.0)
                print(f'====WELCOME  to JP BANK '.upper())
                # importing date and time
                print("Today's date is == :", currentDate)
                print("Your time is ==", currentTime)
                print("********************************")
                print("********************************")
                bankingOperation(user)

            else:
                print('\nInvalid account or password')
                login()
    except ValueError:
            print("Enter a correct number")
            initalization()
    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integer")
        initalization()
    


def registeration():
    print('=== REGISTER BELOW ===')

 
    email = input("Enter your email address\t\n")
    firstName = input("Enter your first name\t\n")
    lastName = input("Enter your last name\t\n")
    password = getpass("Enter your passwordt\n")

    accountNumber = generateAccountNumber()
    
    
     
    isUserCreated = database.create(accountNumber, firstName, lastName, email, password)

    if isUserCreated:
        print(f"{firstName}  Your account creation is successfull\n")
        print(" ====== ====== ====== ====== =====")
        print(f'Your account number is {accountNumber}\n')
        print("Keep your account number  safe ")
        
        login()

    else:
        print("Something went wrong, please try agian")
        registeration()


def bankingOperation(user):
    print(f"Welcome {user[0]}, {user[1]}")
    print(""" What will you want to do 
        1. Deposit
        2. Withdrawal
        3. Complaint
        4. Logout

    """)
  
    optionSelected =  int(input(">>  "))
    
   
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

 
def withdrawalOperation():
    print("How much would you like to withdraw?\n")
    print("********************************")
    # get current balance
    # get amount to withdraw
    # check if the current balace > withdraw balance
    # deduct withdraw amount from the current balance
    # display current balance
    try:
        withdraw = float(input("Enter your amount\t "))
        print("********************************")
        print("Take your cash, %d" %withdraw)

    except ValueError:
        print('Invalid option: Try again later')
        return withdrawalOperation()
    return bankingOperation()

def depositOperation():
    # Get current balance:
    #  Get amoount to deposit
    #  add deposited to the current balaance
    #  display current balance
    print(f'Your deposit is succesfull')
    print(f' Do you want to perform an operation')
    #if yes go to bank operations and if no go to exit

def setCurrentBalance(database, balance):
    database[4] = balance

def getCurrentBalance(database):
    return database[4]

def complaintOperation():
        print("What issue will you like to report")
        print("********************************")
        complaint = input("Enter your complaint\n")
            # database2 = [Complaint]  for 
        print(" Thank you for contacting us")
        print("********************************")
        return bankingOperation()


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
            return logout()
    except ValueError:
        print('Invalid Selection. Try again')
    return logout()



############### SYSTEM INITIALIZATION ###################
initalization()


