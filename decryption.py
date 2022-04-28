"""
Decryption function

Caesar Cipher decryption rule is x = (c - n) % 26
"""


def decrypt(text, shift_amount):
    plain_text = ""

    # Transverse the encrypted/cipher text
    for c in text:
        # print("Transverse list = " + c)
        # Decrypt the capital letter/uppercase alphabet in the cipher text
        if c.isupper():
            # Find the current index/position of c in the range of 0 - 25 (A to Z)
            c_index = ord(c) - ord("A")  # i.e., if "A", c_index = 0 ; if "B", c_index = 1 and so on

            # Perform the negative shift
            new_index = (c_index - shift_amount) % 26  # i.e., if shift 3, "D" becomes "A", thus nex_index is 0

            # Get the new ASCII and convert it to a character
            new_character = chr(new_index + ord("A"))  # i.e., 0 + 65 = 65, ASCII 68 is "A"

            # Append to plain string
            plain_text += new_character

            # Alternatives
            # plain_text += chr((((ord(c) - ord("A")) - shift_amount) % 26) + ord("A"))
            # plain_text += chr((((ord(c) - shift_amount) % 65) % 26) + 65)

        # Encrypt the small letter/lowercase alphabet in the cipher text
        elif c.islower():
            plain_text += chr((((ord(c) - ord("a")) - shift_amount) % 26) + ord("a"))
            # plain_text += chr((((ord(c) - shift_amount) % 97) % 26) + 97)

        # Decrypt the digit in the cipher text
        elif c.isdigit():
            plain_text += chr((((ord(c) - ord("0")) - shift_amount) % 26) + ord("0"))
            # plain_text += chr((((ord(c) - shift_amount) % 48) % 26) + 48)

        # Since character is not an uppercase, lowercase or a digit, leave it as it is
        else:
            # Append to the plain string
            plain_text += c  # same as plain_text = plain_text  + c
    return plain_text
