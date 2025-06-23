import random
import string
import re

class PasswordApp:
    """ Main class that handles password generation and strength checking. """
    
    def menu(self):
        
        """
        Displays a menu for the user and returns their selected choice.
        Returns:
            int: The user's menu choice (1, 2, or 3).
        """
        
        while True:
            the_menu = """Choose from the menu: 
1. Generate Password
2. Check the Strength of Your Password
3. Exit
Please enter the number corresponding to your choice: 
"""
            try:
                choice_menu = int(input(the_menu))
                if choice_menu in [1, 2, 3]:
                    return choice_menu
                else:
                    print('Error, Please try again.')
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Generate Password
    def get_num_pass(self):
        
        """
        Asks the user for the number of passwords to generate (1-5).
        Returns:
            int: Number of passwords to generate.
        """
        
        while True:
            password_num = input('Please enter a number of passwords that you want (1-5): ')

            if password_num == '':
                print("No number entered, using default value of 1.")
                return 1

            try:
                password_num = int(password_num)
                if password_num <= 5 :
                    return password_num
                else:
                    print("Error: num of Passwords must be between 1 and 5!")
            except ValueError:
                print("Please enter a valid number.")

    def password_length(self):
        
        """
        Asks the user for the desired password length (8-16).
        Returns:
            int: The password length.
        """
        
        while True:
            pass_length = input('Please enter a valid length (8-16): ')

            if pass_length == '':
                print("No length entered, using default value of 12.")
                return 12

            try:
                pass_length = int(pass_length)
                if 8 <= pass_length <= 16:
                    return pass_length
                else:
                    print("Error: Password length must be between 8 and 16!")
            except ValueError:
                print("Please enter a valid number.")

    def generate_pass(self, pass_length):
        
        """
        Generates a strong password of the specified length.
        Args:
            pass_length (int): The length of the password to generate.
        Returns:
            str: A generated password.
        """
        
        chars_upper = string.ascii_uppercase
        chars_lower = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation

        password = [
            random.choice(chars_upper),
            random.choice(chars_lower),
            random.choice(numbers),
            random.choice(symbols)
        ]

        password += random.choices(chars_upper + chars_lower + numbers + symbols, k = pass_length - 4)
        random.shuffle(password)
        password = "".join(password)

        return password

    def passwords(self):
        
        """ Generates and prints a list of random passwords based on user input. """
        
        num = self.get_num_pass()
        length = self.password_length()

        print("\nGenerated Passwords:")
        for i in range(1, num + 1):
            print(f"{i}. {self.generate_pass(length)}")
    
    @staticmethod
    def has_upper(password):
        
        """ Check if password has at least one uppercase letter. """
        return bool(re.search(r'[A-Z]', password))
    
    @staticmethod
    def has_lower(password):
        """ Check if password has at least one lowercase letter. """
        return bool(re.search(r'[a-z]', password))

    @staticmethod
    def has_number(password):
        """ Check if password has at least one digit. """
        return bool(re.search(r'[0-9]', password))

    @staticmethod
    def has_symbol(password):
        """ Check if password has at least one special character. """
        return bool(re.search(r'[^a-zA-Z0-9]', password))

    def check_password_strength(self):
        
        """ 
        Checks the strength of a user-provided password and suggests help if weak.
        
        to  make a strong pass you must do:
            1- the len must be more than 8 
            2- the pass must have upper and lower chars
            3- the pass must have symbols
        """
        
        password = input('Please enter your pass that you want to check: ')
        # check if the pass contains certain criteria
        pass_length = len(password)  # len of pass
        pass_has_char_upper = self.has_upper(password)  # upper chars
        pass_has_char_lower = self.has_lower(password)  # lower chars
        pass_has_number     = self.has_number(password) # numbers
        pass_has_symbols    = self.has_symbol(password)  # symbols

        # calculate strength
        strength = 0
        strength_length_password_12 = 12
        strength_length_password_8 = 8
        strength_less = 5
        Very_Strong = 10
        Strong = 7
        
        if pass_length >= strength_length_password_12:
            strength += 3
        elif pass_length >= strength_length_password_8:
            strength += 2
        else:
            strength += 1

        if pass_has_char_upper and pass_has_char_lower:
            strength += 4

        if pass_has_number:
            strength += 2

        if pass_has_symbols:
            strength += 2

        if strength >= Very_Strong:
            print("Your password is Very Strong!")
        elif strength >= Strong:
            print("Your password is Strong!")
        elif strength >= strength_less:
            self.ask_for_help()
        else:
            self.ask_for_help()

    def ask_for_help(self):
        """ Offers help to the user for improving a weak password. """
        
        yes = 'y'
        no = 'n'
        while True:
            user_input = input("You can make your password stronger. Do you need help [Y/N]? ").lower()
            if user_input == yes:
                choice = self.menu()
                if choice == 1:
                    self.passwords()  # Generate passwords
                elif choice == 2:
                    self.check_password_strength()  # Re-run the strength check
                elif choice == 3:
                    print("Exiting program. Goodbye!")
                    break  # Exit program
            elif user_input == no:
                print("Okay, no problem. Thanks for using.")
                break  # Exit loop if user opts not to get help
            else:
                print("Invalid input. Please enter Y or N.")
class Run(PasswordApp):
    
    """ Class that runs the PasswordApp by starting the main loop. """
    
    def start(self):
        
        """ Starts the app and handles user interaction based on menu choices. """
        
        while True:
            choice = self.menu()
            
            if choice == 1:
                self.passwords()
            elif choice == 2:
                self.check_password_strength()
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")