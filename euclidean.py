#!/usr/bin/env python3

import numpy as np
import cipher


def getDecryptedTextWithCurrentKey(key):
    entireDecryptedString = ""
    encryptedFile = open("encrypted.txt", "r")

    for line in encryptedFile:
        entireDecryptedString += cipher.decrypt(line, key)

    encryptedFile.close()
    return entireDecryptedString


def getEntireKnownText():
    entireKnownString = ""
    pfile = open("plain.txt", "r")

    for line in pfile:
        for letter in line:
            letter = letter.lower()
            entireKnownString += letter

    return entireKnownString


def euclideanDistance(key):
    """
    A function to return the euclidean distance between two strings

    ## the longest distance from one point to another is 13 (ie a-n)
    ## Consider the example for forward distance larger than 13 :
    ## ex:  a-o = 14,
    ## 14>13 --> how_much_back = 14-13 =1
    ## back_distance = 13 - how_much_back = 12

    key is equivalent to individual

    Parameters:
    (string) knownText
    (string) decryptedText
    """

    knownText = getEntireKnownText()

    decryptedText = getDecryptedTextWithCurrentKey(key[0])
    distanceArray = []

    for knownLetter, decryptedLetter in zip(knownText, decryptedText):
        forward_dist = abs(ord(knownLetter) - ord(decryptedLetter))

        if(forward_dist > 13):
            how_much_back = forward_dist - 13
            back_distance = 13 - how_much_back
            distanceArray.append(back_distance)
        else:
            distanceArray.append(forward_dist)

    distanceArray = np.array(distanceArray)

    return np.sqrt(np.sum(np.square(distanceArray)))
