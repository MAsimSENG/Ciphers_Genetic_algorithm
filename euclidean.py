
#!/usr/bin/env python3
 
 
import os
from python_speech_features import mfcc
import librosa as li
import numpy as np
from math import*
from decimal import Decimal



 

def euclidean_distance(x,y):
    
 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

 
def main():
 
    """ the main function to create Similarity class instance and get used to it """
 
 
    print (euclidean_distance(["a","b","c","d"],["a","b","c","d"]))
    
if __name__ == "__main__":
    main()
