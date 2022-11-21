def check_key(plain,key):
	if len(plain)==len(key):
		return True
	else:
		return False

def encrypt(plain,key):
	encrypted = ""
	if check_key(plain,key)==False:
		print("Invalid key!!!!!")
		return
	else:
		for p,k in zip(list(plain),list(key)):
			new = ((ord(p)-65) + (ord(k)-65))%26 + 65
			encrypted+=chr(new)
		return encrypted

def decrypt(cipher,key):
	decrypted = ""
	for p,k in zip(list(cipher),list(key)):
		new = ((ord(p)-65) - (ord(k)-65) + 26 )%26 + 65
		decrypted+=chr(new)
	return decrypted

name = "SUSHRINADHAKAL"
key = "VERMANCIPHERXX"

print("Original Text: "+name)
print("Key: "+key)
cipher = encrypt(name,key)
plain = decrypt(cipher,key)
print("After Encryption,Cipher text is: "+cipher)
print("After Decryption,Plain text is: "+plain)

