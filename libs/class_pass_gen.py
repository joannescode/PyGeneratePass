import random
import string
import os
import time
import getpass

class PassGen():
    def __init__(self) -> None:
        self.password_length = None 

    def get_length_password(self):
        self.password_length = int(getpass.getpass("Please enter the number of characters you want in your password.\n"))
             
        if self.password_length > 14:
            print("Enter a password that is 14 characters or less. You don't want to crash the program, right?")
            time.sleep(5)
            os.system('clear')
            return self.get_length_password()
        
    def get_random_string(self):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        numbers = string.digits
        especial_strings = string.punctuation

        all_characters = lowercase_letters + uppercase_letters + numbers + especial_strings
        self.result_password = ''.join(random.choice(all_characters) for _ in range(self.password_length))
        self.password_generated = self.result_password.replace(self.result_password, "***********")
        
    def interation_with_user(self):
        print("Password generated is sucessful:", self.password_generated, "\n")
        print("You wish see your password?")
        print("Press 1, for yes...")
        print("Press 2, for exit...")
        
        user_response = int(input("Option:"))
        print("\n")
        if user_response == 1:
            print(self.result_password)
        else:
            print("Exiting for system...")
            time.sleep(4)
            os.system('clear')
            pass


# Exemplo de uso:
passgen = PassGen()
passgen.get_length_password()
passgen.get_random_string()
passgen.interation_with_user()