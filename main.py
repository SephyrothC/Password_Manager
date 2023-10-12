from psw_check import *
from psw_generator import *


def password_checker(psw):

    if check_psw_in_dataBase(psw):
        while True:
            res = input("Do you want a new password ? Y/N \n")
            if res == 'Y':
                password_generator()
                break
            elif res == 'N':
                break

    elif check_password_in_Web(psw):
        while True:
            res = input("Do you want a new password ? Y/N \n")
            if res == 'Y':
                password_generator()
                break
            elif res == 'N':
                break

    else:
        score = check_secure(psw)
        if score <= 50:
            print("Your password is to low")
            while True:
                res = input("Do you want a new password ? Y/N \n")
                if res == 'Y':
                    password_generator()
                    break
                elif res == 'N':
                    break
        elif score <= 80:
            print("Your password is ok for non-vital accounts")
            while True:
                res = input("Do you want a new password ? Y/N \n")
                if res == 'Y':
                    password_generator()
                    break
                elif res == 'N':
                    break
        else:
            print("Your password is strong")


def main():
    while True:
        option = input(
            '\nWhat option do you want (type the option number): \n 1 : check my password security \n 2 : create a password\n(-1 to exit)\n')

        if option == '-1':
            break
        elif option == '1':
            password_checker(input("Enter your password :\n"))
        elif option == '2':
            password_generator()


if __name__ == '__main__':
    main()
