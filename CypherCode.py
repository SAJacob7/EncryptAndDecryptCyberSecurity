def encrypt_cipher(text, shift):
    new_encryption = ""
    for letter in text:
        if letter.isupper():
            new_letter = chr((ord(letter) + shift-65) % 26 + 65)
        else:
            new_letter = chr((ord(letter) + shift-97) % 26 +97)
        new_encryption += new_letter
    return new_encryption

def decrypt_cipher(text, shift):
    encrypted_message = ""
    for letter in text:
        if letter.isupper():
            encrypted_letter = chr((ord(letter) - (shift-65)) % 26 + 65)
        else:
            encrypted_letter = chr((ord(letter)-97-shift+26)%26 + 97)
        encrypted_message += encrypted_letter
    return encrypted_message

def main():
    encrypt_or_decrypt = str(input("Encrypt (E) or Decrypt (D): "))
    if encrypt_or_decrypt == "E":
        text = str(input("Enter text to encrypt: "))
        shift = int(input("Enter number for shift: "))
        print(encrypt_cipher(text, shift))
    else:
        text = str(input("Enter text to decrypt: "))
        shift = int(input("Enter number for shift: "))
        print(decrypt_cipher(text, shift))

main()