# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:04:12 2021

@author: Geoff

This problem was asked by Square.

Given a string and a set of characters, return the shortest substring 
containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters 
{a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, 
return null.

# Note: I'm just returning an empty string instead of null.

"""

s = "figehaeci"
chars = ['a', 'e', 'i']

def shortest_substring(s, chars):

    start_idx = -1
    best_substring = ''
    best_len = 9999
    still_needed = chars.copy()
    
    i = 0
    
    while i < len(s):
        
        if s[i] in chars and start_idx == -1:
            start_idx = i
            still_needed.remove(s[i])
            
        elif s[i] in still_needed:
            still_needed.remove(s[i])
            
            if len(still_needed) == 0:
                sub = s[start_idx:i+1]
                
                # Test for shortest substring
                if len(sub) < best_len:
                    best_substring = sub
                    best_len = len(best_substring)
                       
                i = start_idx
                start_idx = -1
                still_needed = chars.copy()
    
        i += 1
        
    return best_substring
    
print(shortest_substring(s, chars))
print(shortest_substring('flimflamifloopy', ['f', 'm', 'a']))
print(shortest_substring('Wethepeople', ['x', 'y', 'z']))

