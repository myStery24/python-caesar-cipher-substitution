# Encryption & Decryption using Substitution Algorithm
A Python program that encrypts the original string (plaintext) and decrypts the ciphertext (encrypted string) using a substitution algorithm. The program prompts users to choose between two options: encryption or decryption. Next, users input a message (plaintext/ciphertext) and a shift amount. The message can contain any alphabets/characters (A/a to Z/z), numbers/integers and special characters, while the shift amount accepts only number/integer. Additionally, this program accepts a message up to a length limitation of 100 characters only. With that said, if users enter more than this limit, this program will throw an error message. 

### Features
- Encryption: Encrypt strings with a shift amount.
- Decryption: Decrypt strings with a shift amount.

### Files
| Name             | Description                                                               |
|------------------|---------------------------------------------------------------------------|
| caesar_cipher.py | Contains the `main()` function. Execute this file.                        |
| common.py        | Contains the `menu()` and `check_special_char()` functions.               |
| decryption.py    | Contains `decrypt()` function to decrypt the ciphertext to the plaintext. |
| encryption.py    | Contains `encrypt()` function to encrypt the plaintext to the ciphertext. |

### References
| No. | Website                                                                                                                                                                                                                                                  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.  | [CAESAR CIPHER : PYTHON IMPLEMENTATION](https://medium.com/@lazyendian_bit/caesar-cipher-python-implementation-982593f1ab45)                                                                                                                             |
| 2.  | [Iterating a Python Cipher from Scratch](https://tsmith6421.medium.com/iterating-a-python-cipher-from-scratch-b47f601ca74a)                                                                                                                              |
| 3.  | [Caesar Cipher in Python (Text encryption tutorial)](https://likegeeks.com/python-caesar-cipher/?msclkid=09d01201c6a411eca75e7bbcfa2e48b1)                                                                                                               |
| 4.  | [Cryptography with Python - Caesar Cipher](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm?msclkid=09cfa17bc6a411ecaadc347000f279a6)                                                                  |
| 5.  | https://en.wikipedia.org/wiki/Caesar_cipher                                                                                                                                                                                                              |
| 6.  | [How to Check if a String Contains Special Characters in Python](https://www.knowprogram.com/python/check-special-character-python/?msclkid=1ca6b6c7c69811ecba11c68153753538)                                                                            |
| 7.  | [ASCII Table](https://ascii-tables.com/#:~:text=Standard%20%EE%80%80ASCII%20table%EE%80%81%20contains%20a%20%EE%80%80table%EE%80%81%20of%20127,255%20codes.%20It%20is%20using%20for%20higher-level%20encoding.?msclkid=9b1da445c6aa11ec909368ceca452f8f) |
