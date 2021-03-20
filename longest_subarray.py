# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:34:30 2021

@author: Geoff
"""

'''
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray 
where all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the 
longest subarray of distinct elements is [5, 2, 3, 4, 1].
'''

array1 = [5, 1, 3, 5, 2, 3, 4, 1]
# [5, 2, 3, 4, 1]
array2 = [2, 5, 8, 3, 4, 6, 7, 5]
# [2, 5, 8, 3, 4, 6, 7]

def longest_subarray(array_in):
    
    arr = array_in
    length = len(arr)
    sub_len = length
    index = 0
    
    while True:
        
        total = 0
        for num in arr: 
            total += arr.count(num)
            
        if total == len(arr):
            break
        
        else: 
            index += 1
            
            if index + sub_len > length:
                index = 0; sub_len -= 1
                
        arr = array_in[index:sub_len + index]
    
    return arr
        
print(longest_subarray(array1))
print(longest_subarray(array2))
    
    