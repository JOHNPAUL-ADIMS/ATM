#create records
#update records
#read record
#delete record

#IT IS CALLED CRUD OPPERATION.add()

#search for user
import os #allows us to delete a file
import validation



userdatabasepath = "data/userRecord/"


def create(userAccountNumber, firstName, lastName, email, password, bal):
    #create a file
    #name of file would be accountnumber.txt
    # add the user details to the file
    # return true
    # if saving to  file, delete th file


    userData = firstName + "," + lastName + "," + email + "," + password + "," + str(bal)

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

    fx = open(userdatabasepath + userAccountNumber + ".txt", 'r')

    user_info = fx.readline().split(",")

    fx.close()

    return user_info


def update(userAccountNumber, op, amount):

    fname = read(userAccountNumber)[0]
    lname = read(userAccountNumber)[1]
    email = read(userAccountNumber)[2]
    pword = read(userAccountNumber)[3]
    current_amount = int(read(userAccountNumber)[-1])

    

    if op == 'deposit':

        current_amount += int(amount)

        data = f"{fname},{lname},{email},{pword},{current_amount}"

        f = open(userdatabasepath + str(userAccountNumber) + '.txt', 'w')

        f.write(data)

        print(f"Your Current Balance is:\t#{current_amount}")

        f.close()


        return True

    elif op == 'withdraw' or op == 'transfer':

        current_amount -= int(amount)

        data = f"{fname},{lname},{email},{pword},{current_amount}"

        f = open(userdatabasepath + str(userAccountNumber) + '.txt', 'w')

        f.write(data)

        print(f"Your Current Balance is:\t#{current_amount}")

        f.close()


        return True

    else:
        return "Unknown Action"



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

        f = open(userdatabasepath+accountNumber+".txt", 'r')

        deets = f.readline()

        user_deets = deets.split(",")
        
        if int(password) == int(user_deets[3]):

            return True

            f.close()

        else:

            return False

            f.close()
    





# print(doesEmailExist('johnpauladimonyemma@gmail.com'))
# # print(userdatabasepath)
# # print(read)
# # print(allUsers)
