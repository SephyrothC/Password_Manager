import interface


# def main():

#     while True:

#         option = input(
#             '\nWhat option do you want (type the option number): \n 1 : check my password security \n 2 : create a password\n 3 : transform sentence in password\n(-1 to exit)\n')

#         if option == '-1':  # If the user enters -1
#             break  # Break out of the loop and end the program
#         elif option == '1':  # If the user enters 1
#             # Call the function password_checker with the user's input as a parameter
#             a = input("Enter your password :\n")
#             password_checker(a)
#         elif option == '2':  # If the user enters 2
#             password_generator()  # Call the function password_generator to generate a new password
#         elif option == '3':  # If the user enters 3
#             # Call the function sentence_transformation with the user's input as a parameter
#             a = input("Enter your sentence :\n")
#             santence_tranformation(a)
#         else:
#             print("Error : input invalid !")

#     exit()


if __name__ == '__main__':
    menu = interface.App()
    menu.run()
