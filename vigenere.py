def equal_string(string, keyword):
	if len(string) > len(keyword):
		mod = len(string) % len(keyword) 
		keyword = keyword * (len(string) // len(keyword)) 
		if mod != 0:
			keyword = keyword + keyword[:mod]
	else:
		keyword = keyword[:len(string)]
	return keyword



def encrypt_vigenere(plaintext, keyword):
	ciphertext = ""
	keyword = equal_string(plaintext, keyword)
	for i in range(len(plaintext)):
		if 65 <= (ord(plaintext[i])) <= 90:
			if (ord(plaintext[i]) + ord(keyword[i]) - 65) <= 90:
				ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 65)
			else:
				ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 91)
		else:
			if (ord(plaintext[i]) + (ord(keyword[i]) - 97)) <= 122:
				ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 97)
			else:
				ciphertext = ciphertext + chr(ord(plaintext[i]) + ord(keyword[i]) - 123)
	return ciphertext


def decrypt_vigenere(ciphertext, keyword):
	plaintext = ""
	keyword = equal_string(ciphertext, keyword)
	for i in range(len(ciphertext)):
		if 65 <= (ord(ciphertext[i])) <= 90:
			if (ord(ciphertext[i]) - ord(keyword[i])  + 65) >= 90:
				plaintext = plaintext + chr(ord(ciphertext[i]) - ord(keyword[i]) + 65)
			else:
				plaintext = plaintext + chr(ord(ciphertext[i]) - ord(keyword[i]) + 91)
		else:
			if (ord(ciphertext[i]) - ord(keyword[i]) + 97) >= 122:
				plaintext = plaintext + chr(ord(ciphertext[i]) - ord(keyword[i]) + 97)
			else:
				plaintext = plaintext + chr(ord(ciphertext[i]) - ord(keyword[i]) + 123)
	return plaintext
	



print(en
	encrypt_vigenere(input("Enter a word: "), input("Enter a key word: ")))