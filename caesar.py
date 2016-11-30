def encrypt_ceasar(plaintext):
	ciphertext = ""
	for i in range(len(plaintext)):
		if (88 <= ord(plaintext[i]) <= 90) or (120 <= ord(plaintext[i]) <= 122):
			ciphertext = ciphertext + chr(ord(plaintext[i]) - 23)
		else:
			ciphertext = ciphertext + chr(ord(plaintext[i]) + 3)
	return ciphertext



def decrypt_ceasar(ciphertext):
	plaintext=""
	for i in range(len(ciphertext)):
		if (65 <= ord(ciphertext[i]) <= 67) or (97 <= ord(ciphertext[i]) <= 99):
			plaintext = plaintext + chr(ord(ciphertext[i]) + 23)
		else:
			plaintext = plaintext + chr(ord(ciphertext[i]) - 3)
	return plaintext	



print(encrypt_ceasar(input()))