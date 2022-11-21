def encrypt(full_name,key):
    encrypted = ""
    for char in full_name:
        if char.isupper():
            new = ord(char) + 3
            if new > 90:
                new = new - 90 + 65 - 1
            encrypted = encrypted + chr(new)
        elif char.islower():
            new = ord(char) + 3
            if new > 122:
                new = new - 122 + 97 + 1
            encrypted = encrypted + chr(new)
    return encrypted

def decrypt(encrypted,key):
    decrypted = ""
    for char in encrypted:
        if char.isupper():
            new = ord(char) - 3
            if new < 65:
                new = new + 90 - 65 + 1
            decrypted= decrypted + chr(new)
        elif char.islower():
            new = ord(char) - 3
            if new < 97:
                new = new + 122 - 97 + 1
            decrypted = decrypted + chr(new)
    return decrypted
    
    
full_name = "Sushrina Dhakal"
print("Full name before encryption: "+full_name)

# key = int(input("Enter the key for Encryption and Decryption:"))
key = 3

encrypted = encrypt(full_name,key)
print("After Encryption: Cipher text is "+encrypted)
print("After Decryption: Plain text is "+decrypt(encrypted,key))