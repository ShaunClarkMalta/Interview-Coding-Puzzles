# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 16:50:40 2025

@author: Shaun
"""

'''Input: Array
candidate = ""
count = 0
for i in integer:
    if i == candidate; count +1
    else; count -1;; Count == 0; new candidate
At end: .count(candidate) >= length/2?
'''

def majority_element(this_list):
    candidate = 0
    count = 1
    
    for i in this_list:
        if i == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = i
                count +=1
    if (this_list.count(candidate)) > (len(this_list)/2):
        return candidate
    else:
        return -1
    
test1 = [2,4,8,2,3,2,1,5,4,2,2,7,9]
test2 = [7,3]
test3 = [1]
test4 = [3,4,3]
test5 = [2,4,5,2,2,2,1,3,4,2,2,2,7]

print(f"Test List 1 - Majority: {majority_element(test1)}")
print(f"Test List 2 - Majority: {majority_element(test2)}")
print(f"Test List 3 - Majority: {majority_element(test3)}")
print(f"Test List 4 - Majority: {majority_element(test4)}")
print(f"Test List 5 - Majority: {majority_element(test5)}")