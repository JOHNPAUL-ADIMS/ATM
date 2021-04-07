#GLOBAL 

from datetime import time
from os import P_NOWAIT
from babel import numbers
import random
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
    print("Welcome to the BANK OF JP")
    ownAccount = int(input("Do you have an account with us?\n If (yes) enter 1\n If (no) enter 2. \n Enter your Option  \n "))
    if (ownAccount == 1):
        
        login()
    elif(ownAccount == 2):
       
        print(registeration())
    else:
        print("You have selected invalid option")
    initalization()


def registeration():
    print('=== CLICK BELOW TO REGISTER ===')
    email = input("Enter your email address\n")
    firstName = input("Enter your first name\n")
    lastName = input("Enter your last name\n")
    password = input ("Create a password\n")
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
            # else:
            #     print("Invalid account or password, Enter your correct account Number")
            #     login()
    print('Invalid account or password')
    login()
    
def bankingOperation(user):
    print(f"Welcome {user[0]}")
    optionSelected =  int(input("What will you want to do\n (1) Deposit\n (2) Withdrawal\n (3)Complaint\n (4) Logout\n (5)exit\n"))
    if(optionSelected == 1):
        depositOperation()
    elif(optionSelected == 2):
        withdrawalOperation()
    elif(optionSelected == 3):
        complaintOperation ()
    elif (optionSelected == 4):
        logout()
    elif(optionSelected == 5):
        exit()
    else:
        print("Invalid option selected")
        bankingOperation(user)

def withdrawalOperation():
    print("How much would you like to withdraw?\n")
    print("********************************")
    withdraw = float(input("Enter your amount\t "))
    print("********************************")
    print("Take your cash, %d" %withdraw)

def depositOperation():       
    print("How much will you like to deposit?\n")
    print("********************************")
    deposit = float(input("Enter your current deposit\n"))
    print("Your Current Balance is %d " %deposit)
    print("********************************")


def complaintOperation():
    print("What issue will you like to report")
    print("********************************")
    complaint = input("Enter your complaint\n")
    # database2 = [Complaint]  for 
    print(" Thank you for contacting us")
    print("********************************")


def logout():
    login()



############### SYSTEM INITIALIZATION ###################
initalization()
