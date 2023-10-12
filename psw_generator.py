import secrets
import string
from psw_check import check_secure


def check_string(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def santence_tranformation(string):
    pass


def password_generator():

    while (True):
        size = input("What size of password do you want (12 is recommended)\n")
        if check_string(size):
            size = int(size)
            break

    # Alphabet generator
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    # Generate password meeting constraints
    while True:
        pwd = ''
        for i in range(size):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            continue
        if check_secure(pwd) >= 50:
            break

    print(f"{pwd}")
