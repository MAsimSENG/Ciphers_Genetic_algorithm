#!/usr/bin/env python3

import numpy as np
import cipher


def euclideanDistance(know_text, decrypted_text):
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

    distanceArray = []

    for knownLetter, decryptedLetter in zip(know_text, decrypted_text):
        forward_dist = abs(ord(knownLetter) - ord(decryptedLetter))

        if(forward_dist > 13):
            how_much_back = forward_dist - 13
            back_distance = 13 - how_much_back
            distanceArray.append(back_distance)
        else:
            distanceArray.append(forward_dist)

    distanceArray = np.array(distanceArray)

    return np.sqrt(np.sum(np.square(distanceArray)))
