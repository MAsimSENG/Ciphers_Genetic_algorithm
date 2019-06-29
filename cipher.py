#!/user/bin/env python3

# Constant
LETTER_SHIFT = 97

def simpleShiftEncrypt(string, shift):
	encrypted = ""
	for letter in string:
		letter = charToIntASCII(letter)
		letter += shift
		encrypted += intToCharASCII(letter)
	print(string)
	print(encrypted)

def charToIntASCII(letter):
	'''
	Shift letters to a=0, b=1, c=2 ... z=25 if LETTER_SHIFT == 97
	Shift letters to a=1, b=2, c=3 ... z=26 if LETTER_SHIFT == 96
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

# def intToCharASCII(letter):
# 	'''
# 	Only use if LETTER_SHIFT == 96
# 	Takes an integer and returns a character
# 	Shift letters a=97,b=98,c=99...z=122
# 	'''
# 	if(letter % 26 == 0):
# 		return 'a'
# 	else:
# 		return chr((letter % 26) + LETTER_SHIFT)

if __name__ == '__main__':
    simpleShiftEncrypt('abcdz',27)
