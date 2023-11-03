import requests
import hashlib
import string
import math


FILENAME = "../data/data.csv"


def check_secure(password):

    # Initialized
    score = 0
    entropia = 0

    letters_up = string.ascii_uppercase
    letters_low = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation

    # Check if the password contain everything
    if (any(char in letters_up for char in password)):
        score += len(letters_up)
    if (any(char in letters_low for char in password)):
        score += len(letters_low)
    if (any(char in digits for char in password)):
        score += len(digits)
    if (any(char in special_chars for char in password)):
        score += len(special_chars)

    # calculate the entropia
    if (score != 0):
        entropia = len(password)*math.log(score, 2)

    return entropia


def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.read().splitlines():
            data.append([line])
    return data


def check_password_in_Web(password):

    leak = False

    # Hash the password using SHA-1 algorithm
    password_hash = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()

    # Make a request to "Have I Been Pwned" API to check if the password has been leaked
    response = requests.get(
        f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

    # If the response status code is 200, it means the password has been leaked
    if response.status_code == 200:
        # Get the list of hashes of leaked passwords that start with the same 5 characters as the input password
        hashes = [line.split(':') for line in response.text.splitlines()]

        # Check if the hash of the input password matches any of the leaked password hashes
        for h, count in hashes:
            if password_hash[5:] == h:
                # print( f"Password has been leaked {count} times, change your password.\n")
                leak = True
                break

    return leak


# Read the data file
def check_psw_in_dataBase(password):
    # Assign the variable obvious_psw the list of obvious passwords read from the file FILENAME
    obvious_psw = read_data(FILENAME)

    # For each password psw in the list obvious_psw
    for psw in obvious_psw:
        # If the first element of psw is equal to the password given as a parameter
        if psw[0] == password:
            # Print a warning message indicating that the password is too common and that it should be changed
            # print(
            #     "Your password is in the most common passwords used please change your password\n")
            # Return the value True to indicate that the password is in the database
            return True

    # If no password is equal to the password given, return the value False to indicate that the password is not in the database
    return False
