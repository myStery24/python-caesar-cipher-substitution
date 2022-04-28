from string import punctuation

# Selection menu


def menu():
    print("------------------------------------------------------")
    print("Encryption and Decryption Using Substitution Algorithm")
    print("------------------------------------------------------")
    print("\n>> PLEASE SELECT AN OPTION\n")
    print("Encrypt your message - Press 1")
    print("Decrypt your message - Press 2")

# Check whether the strings (text entered by users) contain any special characters


def check_special_char(text):
    special_char = set(punctuation)

    if any(char in special_char for char in text):
        print(">> Your message contains special character(s).")
    else:
        return text
