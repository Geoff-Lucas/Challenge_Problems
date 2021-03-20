# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 20:01:04 2021

@author: Geoff

This problem was asked by Pinterest.

At a party, there is a single person who everyone knows, but who does not 
know anyone in return (the "celebrity"). To help figure out who this is, 
you have access to an O(1) method called knows(a, b), which returns True 
if person a knows person b, else False.

Given a list of N people and the above operation, find a way to 
identify the celebrity in O(N) time.
"""

# An O(N) algorithm is actually pretty easy to create here.  Essentially,
# every comparison allows us to eliminate one of the two people compared, 
# leaving us with n - 1 comparisons.  

import random

# Each person known to the dictionary key person is in the accompanying list.
knows_web = {
    'a': ['b', 'c', 'e'],
    'b': ['a', 'c', 'd'],
    'c': [],
    'd': ['a','b','c', 'e', 'f'],
    'e': ['a', 'b', 'c', 'f'],
    'f': ['c','e']
    }

# See the O(1) method in the problem descripttion.  This isn't actually O(1)
# but we're assuming so here.
def knows(a, b):
    if b in knows_web[a]:
        return True
    else:
        return False

# List of the people 
people = ['a', 'b', 'c', 'd', 'e', 'f']
# Start at the first for ease.
a = random.choice(people)

while len(people) > 1:
    
    b = random.choice(people)
    
    # In case the random choice is itself
    while a == b:
        b = random.choice(people)
        
    # If the person knows someone, they can't be the celebrity, remove them
    # and keep going from the other person.
    if knows(a, b):
        people.remove(a)
        a = b
    # If a person doesn't know someone, that someone can't be the celebrity, 
    # remove them
    else:
        people.remove(b)

print(people)