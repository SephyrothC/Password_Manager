import secrets
import string


def password_generator(self, size):
    # Alphabet generator
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    # Generate the password
    pwd = ''


for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))


def main():

    pass


if __name__ == '__main__':
    main()
