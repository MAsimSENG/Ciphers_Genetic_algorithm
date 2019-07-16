#!/user/bin/env python3
import itertools
# Constant
LETTER_SHIFT = 97

def decrypt(text, key):
	'''
	This method determines the type of key (either int, string or list) and calls the necessary function to decrypt the text.
	'''
	if(type(key) == int):
		text_to_return=intDecrypt(text, key)
	elif(type(key) == str):
		text_to_return=strDecrypt(text,key)
	elif(type(key) == list):
		text_to_return=intListDecrypt(text, key)
	else:
		print ('Not supported')
	return text_to_return
def encrypt(text, key):
	'''
	This method determines the type of key (either int, string or list) and calls the necessary function to encrypt the text.
	'''
	if(type(key) == int):
		text_to_return = intEncrypt(text, key)
		return 	text_to_return

	elif(type(key) == str):
		text_to_return = strEncrypt(text,key)
		return 	text_to_return

	elif(type(key) == list):
		text_to_return = intListEncrypt(text, key)
		return 	text_to_return

	else:
		print ('Not supported')
	return 	text_to_return

def strDecrypt(text, key):
	'''
	This method decrypts (shifts) the text by iterating through a string. For this method when the chars are converted into ints, they are increased by +1 to convert a=0 to a=1, b=1 to b=2...(This is only done when LETTER_SHIFT = 97)
	'''
	intKeyList = []
	for letter, i in zip(key, itertools.count(0,1)):
		intKeyList.append(charToIntASCII(letter) + 1)

	text_to_return = intListDecrypt(text,intKeyList)
	return text_to_return

def strEncrypt(text, key):
	'''
	This method encrypts (shifts) the text by iterating through a string. For this method when the chars are converted into ints, they are increased by +1 to convert a=0 to a=1, b=1 to b=2...(This is only done when LETTER_SHIFT = 97)
	'''
	intKeyList = []
	for letter, i in zip(key, itertools.count(0,1)):
		intKeyList.append(charToIntASCII(letter) + 1)

	text_to_return = intListEncrypt(text,intKeyList)

	return text_to_return

def intListDecrypt(text, key):
	'''
	This method decrypts (shifts) the text by iterating through an integer list
	'''
	decrypted = ""
	for letter, shift in zip(text, itertools.cycle(key)):
		decrypted += decryptShiftLetter(letter,shift)

	return decrypted

def intListEncrypt(text, key):
	'''
	This method encrypts (shifts) the text by iterating through an integer list
	'''
	encrypted = ""
	for letter, shift in zip(text, itertools.cycle(key)):
		encrypted += encryptShiftLetter(letter,shift)
	return encrypted

def intDecrypt(text, key):
	'''
	This method decrypts (shifts) the text by a constant amount for each letter
	'''
	shift = key
	decrypted = ""
	for letter in text:
		decrypted += decryptShiftLetter(letter,shift)

	return decrypted

def intEncrypt(text, key):
	'''
	This method encrypts (shifts) the text by a constant amount for each letter
	'''
	shift = key
	encrypted = ""
	for letter in text:
		encrypted += encryptShiftLetter(letter,shift)

	return encrypted

def decryptShiftLetter(letter, shift):
	'''
	Shifts a letter by the specified amount
	'''

	letter = charToIntASCII(letter)
	letter -= shift
	letter = intToCharASCII(letter)
	return letter

def encryptShiftLetter(letter, shift):
	'''
	Shifts a letter by the specified amount
	'''
	if(ord(letter) >= 65 and ord(letter) <= 90):
		letter = letter.lower()
	if(ord(letter) >= 97 and ord(letter) <= 122):
		letter = charToIntASCII(letter)
		letter += shift
		letter = intToCharASCII(letter)
	return letter

def charToIntASCII(letter):
	'''
	Shift letters to a=0, b=1, c=2 ... z=25 if LETTER_SHIFT == 97
	returns a number
	'''
	return ord(letter) - LETTER_SHIFT

def intToCharASCII(letter):
	'''
	Only use if LETTER_SHIFT == 97
	Takes an integer and returns a character
	Shift letters a=97,b=98,c=99...z=122
	'''
	return chr((letter % 26) + LETTER_SHIFT)
