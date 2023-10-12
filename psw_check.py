import requests
import hashlib
import string
import math


FILENAME = "donne.csv"


def check_secure(password):

    # Initialized
    score = 0

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
                print(
                    f"Password has been leaked {count} times, change your password.\n")
                leak = True
                break
    else:
        print("Could not check password.\n")

    return leak


def check_psw_in_dataBase(password):
    obvious_psw = read_data(FILENAME)
    for psw in obvious_psw:
        if psw[0] == password:
            print(
                "Your password is in the most common passwords used please change your password\n")
            return True
    return False
