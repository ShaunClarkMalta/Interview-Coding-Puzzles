'''You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]'''

'''Input Lists 1 and 2
for i in range:
    list1 [i] + list2 [i] + carry_flag
    if total > 9:
        carry_flag = True'''

def add_two_numbers(list1, list2):
    carry_flag = 0
    result = []

    #Making local copies so as to leave original intact
    list1 = list1[:]
    list2 = list2[:]

    #Check to see if both lists are the same length. If they are, then proceed, else, must fill with 0s to be the same size
    while (len(list1) != len(list2)):
        if len(list1) < len(list2):
            list1.append(0)
        else: 
            list2.append(0)

    #Both lists are same size. Can begin to add integers, from left to right
    for i in range(len(list1)):
        #if list1[i] + list2[i] + carry > 9; then carry_flag = 1. Else, 0
        total = list1[i] + list2[i] + carry_flag
        if total > 9:
            carry_flag = 1
            total -= 10
            result.append(total)
        else:
            carry_flag = 0
            result.append(total)

    #if at end, there is still a 1 carried, then you need to append this to the end of the results
    if carry_flag ==1:
        result.append(carry_flag)
    return result

l1 = [0]
l2 = [0]
print(f"Results: {add_two_numbers(l1, l2)}")

l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(f"Results: {add_two_numbers(l1, l2)}")

l1 = [2,4,3]
l2 = [5,6,4]
print(f"Results: {add_two_numbers(l1, l2)}")