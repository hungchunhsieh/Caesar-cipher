import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("List all possible Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()

    for shift in range(1, len(alphabet) + 1):
        decrypted_message = ""

        for c in encrypted_message.lower():

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - shift) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c

        print("shifted position: {0}, decrypted message: {1}".format(shift, decrypted_message))

decrypt()