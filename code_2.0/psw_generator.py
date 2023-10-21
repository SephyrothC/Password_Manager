import secrets
import string
from psw_check import *


def check_string(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def santence_tranformation(string):
    # Définir le dictionnaire de correspondances
    leet_dict = {
        "a": "@",
        "b": "8",
        "e": "3",
        "i": "!",
        "l": "|",
        "o": "0",
        "s": "5",
    }

    # Initialize the modified string
    modified_string = ""

    upper = True

    # Loop through each character in the string
    for character in string:
        if str(character) == ' ':
            upper = True
            continue

        if upper:
            character = character.upper()
            upper = False
        # If the character is a letter, convert it to lowercase
        elif character.isalpha():
            # character = character.lower()
            # If the character exists in the dictionary, replace it with its value
            if character in leet_dict:
                character = leet_dict[character]
        # Add the character to the modified string
        modified_string += character

    if not (check_psw_in_dataBase(modified_string)) and not (check_password_in_Web(modified_string)) and check_secure(modified_string) >= 50:
        # Display the modified string
        print(f"Password :{modified_string} \n")
    else:
        print("This sentence is not strong enough")


def password_generator():

    # while (True):
    # Ask the user for the desired password size (12 is recommended)
    # size = 15
    # # Check if the input is a valid number
    # if check_string(size):
    #     # Convert the input to an integer
    #     size = float(size)
    #     if size != round(size):
    #         print("Error : input invalid !")
    #         continue
    #     if size >= 12 and size <= 32:
    #         size = int(size)
    #         break
    # print("Error : input invalid !")
    size = 15
    # Alphabet generator
    # Create a string of all possible characters: letters, digits, and special characters
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    # Generate password meeting constraints
    # Loop until a valid password is generated
    while True:
        # Initialize an empty password
        pwd = ''
        # Loop through the size of the password
        for i in range(size):
            # Add a random character from the alphabet to the password
            pwd += ''.join(secrets.choice(alphabet))

        # Check if the password meets the requirements:
        # - It contains at least one special character
        # - It contains at least two digits
        # If not, generate a new password
        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            continue
        # Check if the password is secure enough using a function that returns a score between 0 and 100
        # If the score is at least 50, break the loop and return the password
        if check_secure(pwd) >= 50:
            break

    # Print the generated password
    return pwd
