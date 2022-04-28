"""
Encryption function

Caesar Cipher encryption rule is c = (x + n) % 26

ASCII code/Unicode
1) uppercase begins with "A" 65 and ends with "Z" 90
2) lowercase begins with "a" 97 and ends with "z" 122
3) integer begins with "0" 48 and ends with "0" 57

ord() converts a character to its numeric representation in Unicode,
ord() accepts a single character and returns the number representing its Unicode
i.e., ord("A") is 65

chr() is the inverse of ord() method
chr() accepts a number representing the Unicode of a character,
and returns the actual character corresponding to the numeric code
i.e., chr(65) is "A"
"""


def encrypt(text, shift_amount):
    cipher_text = ""

    # Transverse the plain text
    for c in text:
        # print("Transverse list = " + c)
        # Encrypt the capital letter/uppercase alphabet in the plain text
        if c.isupper():
            # Find the current index/position of c in the range of 0 - 25 (A to Z)
            c_index = ord(c) - ord("A")  # i.e., if "A", c_index = 0 ; if "B", c_index = 1 and so on

            # Perform the shift
            new_index = (c_index + shift_amount) % 26  # i.e., if shift 3, "A" becomes "D", thus nex_index is 3

            # Get the new ASCII and convert it to a character
            new_character = chr(new_index + ord("A"))  # i.e., 3 + 65 = 68, ASCII 68 is "D"

            # Append to encrypted string
            cipher_text += new_character

            # Alternatives
            # cipher_text += chr((((ord(c) - ord("A")) + shift_amount) % 26) + ord("A"))
            # cipher_text += chr((((ord(c) + shift_amount) % 65) % 26) + 65)

        # Encrypt the small letter/lowercase alphabet in the plain text
        elif c.islower():
            cipher_text += chr((((ord(c) - ord("a")) + shift_amount) % 26) + ord("a"))
            # cipher_text += chr((((ord(c) + shift_amount) % 97) % 26) + 97)

        # Encrypt the digit in the plain text
        elif c.isdigit():
            cipher_text += chr((((ord(c) - ord("0")) + shift_amount) % 26) + ord("0"))
            # cipher_text += chr((((ord(c) + shift_amount) % 48) % 26) + 48)

        # Since character is not an uppercase, lowercase or a digit, leave it as it is
        else:
            # Append to the encrypted string
            cipher_text += c  # same as cipher_text = cipher_text + c
    return cipher_text
