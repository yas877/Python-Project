# Caesar Cipher in Python
# by Shaik Yasmin 

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            # Encrypt uppercase characters
            new_char = chr((ord(char) - 65 + key) % 26 + 65)
            encrypted_text += new_char
        elif char.islower():
            # Encrypt lowercase characters
            new_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += new_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isupper():
            # Decrypt uppercase characters
            new_char = chr((ord(char) - 65 - key) % 26 + 65)
            decrypted_text += new_char
        elif char.islower():
            # Decrypt lowercase characters
            new_char = chr((ord(char) - 97 - key) % 26 + 97)
            decrypted_text += new_char
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char
    return decrypted_text

# Input the plain text and the key for encryption
plain_text = input("Plain text: ")
encryption_key = int(input("Enter key for Encryption: "))

# Encrypt the plain text
cipher_text = encrypt(plain_text, encryption_key)
print("Cipher text: " + cipher_text)

# Input the key for decryption
decryption_key = int(input("Enter key for Decryption: "))

# Decrypt the cipher text
decrypted_text = decrypt(cipher_text, decryption_key)
print("Plain text: " + decrypted_text)
