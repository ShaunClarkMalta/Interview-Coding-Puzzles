'''Given an integer x, return true if x is a palindrome, and false otherwise.

Follow up: Could you solve it without converting the integer to a string?'''

'''First Impression: to convert to string a x == x[::-1]
However, Follow-up suggests another method. Also, to keep in mind that -x can never be a palindrome because of the sign'''

'''
Edge Cases:
    If x < 0; Not palindrome (due to sign)
    x ends in 0 (x/10 == 0); Not a palindrome (0 at end)
    x == 0; Palindrome

x = integer, reversed = 0
while x > 0:
    reversed = reversed*10 + x%10
x == reversed?
'''

def palindrome(number):
    if (number < 0):                                    #Negative numbers are always False because of sign
        return False
    elif (number%10 == 0) and (number!=0):               #Any number ending in 0 is also False
        return False

    rev_number = 0
    x = number                                      #Allows us to use and work with x, whilst still having number to compare at the end
    while (x > rev_number):                         #Only need to check half the digits 
        rev_number = (rev_number*10) + (x % 10)     #This loops through, multiplying rev_number by 10 and adding as the final digit the remained from x/10
        x = x//10
    return (rev_number == x) or (rev_number//10 == x)  #rev_number//10 is in case there is an odd number of digits
        
test1 = 1234321
test2 = 7895987
test3 = 0
test4 = -152
test5 = 123210
print(f"Number {test1} - Palindrome?: {palindrome(test1)}")
print(f"Number {test2} - Palindrome?: {palindrome(test2)}")
print(f"Number {test3} - Palindrome?: {palindrome(test3)}")
print(f"Number {test4} - Palindrome?: {palindrome(test4)}")
print(f"Number {test5} - Palindrome?: {palindrome(test5)}")