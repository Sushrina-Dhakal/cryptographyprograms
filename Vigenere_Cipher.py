def make_key(plain,key):
	if len(plain) == len(key):
		return key
	else:
		for i in range(len(plain) - len(key)):
			key = key+key[i % len(key)]
		return key

def encrypt(plain,key):
	encrypted = ""
	for i in range(len(plain)):
		new = (ord(plain[i]) + ord(key[i])) % 26
		new = new + ord('A')
		encrypted+=chr(new)
	return encrypted

def decrypt(cipher,key):
	decrypted = ""
	for i in range(len(cipher)):
		new = (ord(cipher[i]) - ord(key[i]) + 26) % 26
		new = new + ord('A')
		decrypted+=chr(new)
	return decrypted


name = "SUSHRINADHAKAL"
key = "VIGENERE"

key = make_key(name,key)

print("Original Text: "+name)
cipher = encrypt(name,key)
print("After Encryption,Cipher text is: "+cipher)
plain = decrypt(cipher,key)
print("After Decryption,Plain text is: "+plain)



