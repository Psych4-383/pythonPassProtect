"""
Secure your passwords!!!
"""
import getpass
import pyperclip

def secureMyPassowrd(passwordToSecure):
    """
    This function secures a password.
    """
    passwordToSecure = passwordToSecure.replace('s', '$')
    passwordToSecure = passwordToSecure.replace('and', '&')
    passwordToSecure = passwordToSecure.replace('a', '@')
    passwordToSecure = passwordToSecure.replace('i', '1')
    passwordToSecure = passwordToSecure.replace('o', '0')
    passwordToSecure = passwordToSecure.replace('I', '|')
    return passwordToSecure
    

storeBool = bool(int(input('Type 1 to store password in file, type 0 to remain anonymous\n--> ')))
password = getpass.getpass(prompt = 'Password: ')
if storeBool == False:
    copyBool = bool(int(input('Type 1 to copy\n--> ')))
    if copyBool == True:
        pyperclip.copy(secureMyPassowrd(password))

elif storeBool == True:
    un = input('What is username or keyword for this passowrd (This will be written in the file)\n--> ')
    with open('myPws.txt', 'w') as f:
        f.write(f'{un} - {secureMyPassowrd(password)}')
    copyBool = bool(int(input('Type 1 to copy\n--> ')))
    if copyBool == True:
        pyperclip.copy(secureMyPassowrd(password))