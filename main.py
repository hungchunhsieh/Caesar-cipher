import string

alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"

def decrypt():
    print("List all possible Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    # Test case: "Vjh cqn Oxaln kn frcq hxd!"
    # Answer: "May the force be with you!"

    for shift in range(1, len(alphabet) + 1):
        decrypted_message = shiftMessage(alphabet, encrypted_message, shift)
        print("shifted position: {0}, decrypted message: {1}".format(shift, decrypted_message))

def shiftMessage(alphabet: string, encrypted_message: string, shift: int):
    shifted_message = ""
    
    for c in encrypted_message.lower():
        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            shifted_message += new_character
        else:
            shifted_message += c

    return shifted_message

decrypt()