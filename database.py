#create records
#update records
#read record
#delete record

#IT IS CALLED CRUD OPPERATION.add()

#search for user
import os #allows us to delete a file
import validation
userdatabasepath = "data/userRecord/"


def create(userAccountNumber, firstName, lastName, email, password):
    #create a file
    #name of file would be accountnumber.txt
    # add the user details to the file
    # return true
    # if saving to  file, delete th file


    userData = firstName + "," + lastName + "," + email + "," + password + "," + str(0)
    if doesAccountNumberExist(userAccountNumber):
        return False

    if  doesEmailExist(email):
        print("Email exists")
        return False

    finalisationState = False

    try:    
        f = open(userdatabasepath + str(userAccountNumber) + '.txt', 'x')
        
    except FileExistsError:
        doesFileContainData = read(userdatabasepath + str(userAccountNumber) + '.txt')
        if not  doesFileContainData:
            delete(userAccountNumber)
        print()

        # check content of the file
        #delete(accountNumber)
    else:
        f.write(str(userData))
        finalisationState =  True

    finally:
        f.close()
        return finalisationState
    

def read(userAccountNumber):
    
    isLoginNumberValidation = validation.loginNumberValidation(userAccountNumber)
    
    try:
        if isLoginNumberValidation:
            f = open(userdatabasepath + str(userAccountNumber) + '.txt', 'r')
        else:
            f = open(userdatabasepath + userAccountNumber, "r")
        # r is for read while x is for open
            
    except FileNotFoundError:
        print("user not found")

    except FileExistsError:
        print("User does not exist")
    except TypeError:
        print("Invalid account Number Format")
    else:
        return  f.readline()
    return False

    # find user with the account
    # fetch content of the file


def update(userAccountNumber):
    print()
    # find the user account number
    # fetch the content of the file 
    # update the content of the flile
    # save the file
    # return true



def delete(userAccountNumber):
    # print("Delete user account")
   
    isDeleteSuccesful = False

    if os.path.exists(userdatabasepath + str(userAccountNumber) + ".txt"):
        
        try:
            os.remove(userdatabasepath + str(userAccountNumber) + ".txt")
            isDeleteSuccesful = True
        except FileNotFoundError:
            print("User not found")
        
        finally:
            return isDeleteSuccesful

    # find the user with account number 
    # delete the user record 
    # return true

def doesEmailExist(email):

    allUsers = os.listdir(userdatabasepath)

    for user in allUsers:
        userList = str.split(read(user), ',')
        if email in userList:
            return  True
    return False    

def doesAccountNumberExist(accountNumber):
    allUsers = os.listdir(userdatabasepath)

    for user in allUsers:
        
        if user == str(accountNumber) + ".txt":
            return True
    return False

# def find(userAccountNumber):
#     print("find user")
#     #find user record in the data folder


def authenticateUser(accountNumber, password):

    if doesAccountNumberExist(accountNumber):
        user = str.split(read(accountNumber), ',')

        if password == user[3]:
            return user 
    return False
    





# print(doesEmailExist('johnpauladimonyemma@gmail.com'))
# # print(userdatabasepath)
# # print(read)
# # print(allUsers)
