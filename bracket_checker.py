# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 21:12:46 2021

@author: Geoff
"""

'''
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.
'''

good1 = "([])[]({})"
good2 = "({[()()()]})"
bad1 = "([)]"
bad2 = "((()"

def well_formed_checker(string):

    check_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
        }
    
    closing = "}])"
    brackets = ''
    
    for bracket in string:
        
        # If there is nothing in brackets
        if not brackets:
            brackets = bracket
            
        # There's at least one bracket    
        else:
            
            # If it's a closing bracket, last bracket must be mathcing opening
            # Else it's malformed
            if bracket in closing:
            
                if check_dict[brackets[-1]] == bracket:
                    brackets = brackets[0:-1]
                else:
                    break
            
            # If it's opening, add it to the list
            else:
                brackets += bracket
                
    return not bool(brackets)

well_formed_checker(good1)
well_formed_checker(good2)

well_formed_checker(bad1)
well_formed_checker(bad2)
        