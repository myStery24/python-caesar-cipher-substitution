from common import menu, check_special_char
from encryption import encrypt
from decryption import decrypt


def main():
    # Print a selection menu
    menu()
    # Wait for users' input in integer/number
    option = int(input())

    # If the option is 1, do the encryption
    if option == 1:
        print("\nEncryption")
        # Receive plain text
        message = input("Plain Text = \t")
        # Check character limit
        while len(message) > 100:
            print("You have exceeded the character limit of 100. Please try again.")
            message = input("Plain Text = \t")
        # Check for special characters
        check_special_char(message)
        # Receive shift amount in integer
        key = int(input("Shift amount = \t"))
        # Result
        print("Cipher Text = \t" + encrypt(message, key))

    # If the option is 2, do the decryption
    elif option == 2:
        print("\nDecryption")
        # Receive cipher text
        encrypted_message = input("Cipher Text = \t")
        # Check character limit
        while len(encrypted_message) > 100:
            print("You have exceeded the character limit of 100. Please try again.")
            encrypted_message = input("Cipher Text = \t")
        # Check for special characters
        check_special_char(encrypted_message)
        # Receive shift amount in integer
        key = int(input("Shift Amount = \t"))
        # Result
        print("Plain Text = \t" + decrypt(encrypted_message, key))
    else:
        try:
            # Code that has the potential to cause an exception
            # Raise a TypeError if option is not an integer
            if type(option) is not int:
                raise TypeError("Error! Invalid selection, please enter either 1 or 2.")
            # Check if the option is other than integer 1 and 2
            elif option != 1 or 2:
                print("Error! Press 1 to encrypt or Press 2 to decrypt.\n")
                # Rerun the program
                main()
        except (TypeError, ValueError):
            raise Exception('Invalid entry. Please try again.')


if __name__ == '__main__':
    main()
