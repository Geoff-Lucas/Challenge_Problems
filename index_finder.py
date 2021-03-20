# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 22:07:19 2021

@author: Geoff

This problem was asked by Dropbox.

Given a string s and a list of words words, where each word is the same 
length, find all starting indices of substrings in s that is a concatenation 
of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at 
index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] 
since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

import itertools
import re

def index_finder(words, s):
    
    perms = itertools.permutations(words)
    found = []
    
    for perm in perms:
        joined = "".join(perm)
        
        match = re.finditer(joined, s) 
    
        for m in match:
            found.append(m.start())
            
    return found

s1 = "dogcatcatcodecatdog"
words = ["cat", "dog"]
print(index_finder(words, s1))
# >>> [0, 13]

s2 = "barfoobazbitbyte"
print(index_finder(words, s2))
# >>> []

s3 = "dogcatcatcodedogcatdogcatcodefunwhipple"
words = ["cat", "dog", 'code']
print(index_finder(words, s3))
# >>> [6, 9, 19]