# Text Encryption and Decryption with rule tagging.

# This program encrypts text from a file using custom rules, 
# stores rule tags to avoid ambiguity, decrypts the text, 
# and verifies wheather decryption was successful.

def encrypt_text(shift1, shift2):
    # Open the original text file in read mode
    with open("raw_text.txt", "r") as file:
        text = file.read()

        # Variable to store encrypted result
        encrypted = ""
        # Loop through each character in the original text
    for ch in text:

        # Case 1: Lowercase letters
        if ch.islower():

            # Lowercase first half (a-m)
            if 'a' <= ch <= 'm':
                # Shift forward by shift1 * shift2
                enc = chr((ord(ch) - ord('a') + shift1 * shift2) % 26 + ord('a'))

                # Add rule tag "L1" before encrypted character
                encrypted += "L1" + enc

            # Lowercase second half (n-z)
            else:
                # Shift backward by shift1 + shift2
                enc = chr((ord(ch) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))

                # Add rule tag "L2"
                encrypted += "L2" + enc

        # Case 2: Uppercase letters
        elif ch.isupper():

            # Uppercase first half (A-M)
            if 'A' <= ch <= 'M':
                # Shift backward by shift1
                enc = chr((ord(ch) - ord('A') - shift1) % 26 + ord('A'))

                # Add rule tag "U1"
                encrypted += "U1" + enc

            # Uppercase second half (N-Z)
            else:
                # Shift forward by shift2 squared
                enc = chr((ord(ch) - ord('A') + shift2 ** 2) % 26 + ord('A'))

                # Add rule tag "U2"
                encrypted += "U2" + enc

        # Case 3: Other characters 
        else:
            # Spaces, numbers, symbols are added without change
            encrypted += ch

    # Write encrypted text into encrypted_text.txt
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)


def decrypt_text(shift1, shift2):
    # Open encrypted file
    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted = ""   # Store decrypted result
    i = 0            # Index to traverse encrypted text

    # Loop until end of encrypted text
    while i < len(text):

        # Decrypt lowercase a-m (L1)
        if text[i:i+2] == "L1":
            ch = text[i+2]  # Actual encrypted character
            decrypted += chr((ord(ch) - ord('a') - shift1 * shift2) % 26 + ord('a'))
            i += 3          # Move index past tag and character

        # Decrypt lowercase n-z (L2)
        elif text[i:i+2] == "L2":
            ch = text[i+2]
            decrypted += chr((ord(ch) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))
            i += 3

        # Decrypt uppercase A-M (U1) 
        elif text[i:i+2] == "U1":
            ch = text[i+2]
            decrypted += chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))
            i += 3

        # Decrypt uppercase N-Z (U2) 
        elif text[i:i+2] == "U2":
            ch = text[i+2]
            decrypted += chr((ord(ch) - ord('A') - shift2 ** 2) % 26 + ord('A'))
            i += 3

        # Other characters
        else:
            # Directly add unchanged characters
            decrypted += text[i]
            i += 1

    # Write decrypted text into decrypted_text.txt
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted)


def verify_decryption():
    # Read original file
    with open("raw_text.txt", "r") as f1:
        original = f1.read()

    # Read decrypted file
    with open("decrypted_text.txt", "r") as f2:
        decrypted = f2.read()

    # Compare both contents
    if original == decrypted:
        print("Decryption successful! Files match.")
    else:
        print("Decryption failed! Files do not match.")


def main():
    # Take user inputs for shifts
    shift1 = int(input("Enter shift1 value: "))
    shift2 = int(input("Enter shift2 value: "))

    # Perform encryption
    encrypt_text(shift1, shift2)
    print("Encryption completed successfully.")

    # Perform decryption
    decrypt_text(shift1, shift2)
    print("Decryption completed successfully.")

    # Verify result
    verify_decryption()


# Program execution starts here
main()