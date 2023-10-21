from psw_check import *
from psw_generator import *
import interface


def password_checker(psw):

    # If the password is in the database of obvious passwords
    if check_psw_in_dataBase(psw):
        return "in my data"
        while True:  # Start an infinite loop
            # Ask the user if they want a new password and store their answer in the variable res
            res = input("Do you want a new password ? Y/N \n")
            if res == 'Y' or res == 'y':  # If the user answers yes
                password_generator()  # Call the function password_generator to generate a new password
                break  # Break out of the loop
            elif res == 'N' or res == 'n':  # If the user answers no
                break  # Break out of the loop

    # If the password is not in the database but is found on the web
    elif check_password_in_Web(psw):
        return "in my data"
        while True:  # Start an infinite loop
            # Ask the user if they want a new password and store their answer in the variable res
            res = input("Do you want a new password ? Y/N \n")
            if res == 'Y' or res == 'y':  # If the user answers yes
                password_generator()  # Call the function password_generator to generate a new password
                break  # Break out of the loop
            elif res == 'N' or res == 'n':  # If the user answers no
                break  # Break out of the loop

    else:  # If the password is not in the database and not on the web

        # Call the function check_secure to calculate a score for the password and store it in the variable score
        score = check_secure(psw)

        if score <= 50:  # If the score is less than or equal to 50
            # Print a message indicating that the password is too weak
            return ("to low")
            while True:  # Start an infinite loop
                # Ask the user if they want a new password and store their answer in the variable res
                res = input("Do you want a new password ? Y/N \n")
                if res == 'Y' or res == 'y':  # If the user answers yes
                    password_generator()  # Call the function password_generator to generate a new password
                    break  # Break out of the loop
                elif res == 'N' or res == 'n':  # If the user answers no
                    break  # Break out of the loop

        elif score <= 80:  # If the score is between 50 and 80
            # Print a message indicating that the password is acceptable for non-sensitive accounts
            return ("ok non-vital accounts")
            while True:  # Start an infinite loop
                # Ask the user if they want a new password and store their answer in the variable res
                res = input("Do you want a new password ? Y/N \n")
                if res == 'Y' or res == 'y':  # If the user answers yes
                    password_generator()  # Call the function password_generator to generate a new password
                    break  # Break out of the loop
                elif res == 'N' or res == 'n':  # If the user answers no
                    break  # Break out of the loop

        else:  # If the score is greater than 80
            # Print a message indicating that the password is strong
            return ("strong")
