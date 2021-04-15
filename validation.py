def loginNumberValidation(accountNumber):
    
    if accountNumber:
      
        try:
            if len(str(accountNumber)) == 10:
                return True
        except ValueError:
            return False
        except TypeError:
            return False

    return False


# def registerationvalidation(email, firstName, lastName):

#     try:
#         email, firstName, lastName
#         return True

#     except NameError:
#         print('NameError: Use alphabets')
#         return False
