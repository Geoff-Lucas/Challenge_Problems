# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:06:36 2021

@author: geoff
"""

'''
Each turn the first player guesses some number, and the second player responds by saying how many 
digits in this number correctly matched their location in the secret code. For example, if the secret 
code were 123456, then a guess of 175286 would score two, since 1 and 6 were correctly placed.
Write an algorithm which, given a sequence of guesses and their scores, determines whether there 
exists some secret code that could have produced them.

For example, for the following scores you should return True, since they correspond to the secret code 123456:
{175286: 2, 293416: 3, 654321: 0}

However, it is impossible for any key to result in the following scores, so in this case you should return False:
{123456: 4, 345678: 4, 567890: 4}

'''

good = {175286: 2, 293416: 3, 654321: 0}
bad = {123456: 4, 345678: 4, 567890: 4}

# Brute Force

guesses = bad
verdict = False

for i in range(100000, 1000000):
    
    counter = 0
    for key in guesses.keys():
        score = 0
        
        seq = str(i); guess = str(key)
        
        for j,k in zip(seq, guess):
            if j == k:
                score += 1
                
        if score == guesses[key]:
            counter += 1
    
    if counter == len(guesses):
        verdict = True
        break
    
print(verdict)
                
                
                
                
                
                
        
        
        
         