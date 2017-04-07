#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:28:35 2016

@author: Keerthana
"""
import re

def tobits(s):
    result = []
    for c in s:
        bits = bin(c)[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    print("\n----------------Before Bit Stuffing----------------\n\n\n\n")
    print(len(result))
   # int i,j,k=0,z,n,l;
    
    return result
   
def bitstuff(binval):

  # n=len(binval)
   n=1400
   for i in range(0,n):
        #print("in i for", i)
        if binval[i] == 1:
            k = 1
            
            for j in range(i+1,i+6):
                if(j>n):
                    return binval
                #print("in j loop", j)
                if binval[j] == 1:
                    k = k + 1 
                    print("found 1",k,j,i)
                else:
                    k = 0
                if (k == 5):     
                        print("0000000000000000000000found stuff",i,j)
                        i = i + 5
                        z = n + 1
                        n = z
                        for l in range(z,i,-1):
                            binval[l] = binval[l-1]
                           # print ("stuffing",l,y,binval[l],binval[y])
                            binval[i] = 0
                
   return binval
                
#def bitdestuff(stuffedval):
    
   

def frombits(bits):
    chars = []
    for b in range(len(bits) // 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)
    
    
filename = '/Users/Keerthana/Desktop/networkstext.txt'
with open(filename, 'rb') as f:
    content = f.read()
    #print("--------------------------------------\n\n")
    #print("original text")
    #print(content)
    binaryvalue = tobits(content)
    stuffedvalue = bitstuff (binaryvalue)
    print("\n\n\n\n----------------After Bit Stuffing----------------\n\n")
    print(len(binaryvalue))
    #destuffedval = bitdestuff(suffedvalue)
    asciivalue = frombits(binaryvalue)
    #print("--------------------------------------\n\n")
    #print("ascii text ")
    #print("--------------------------------------\n\n")
    #print(asciivalue)    
    if ( content != asciivalue ):
        print("doesnt matches")
    else:
        print("match")
