'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21'''

'''Similar to Palindrome Integer?
Take number
If < 0, remember to add sign after! //Need flag
Abs |number|
while number > 0:
    - Divide number by 10. Remainder is added to the reverse, and multiplied by 10
'''

def reverse_integer(number):
    negative_flag = False
    reverse = 0
    num = number

    #set flag if negative
    if number < 0:
        negative_flag = True
        num = abs(number)

    #Do loop, transferring the digits from num to reverse.
    #This will be done in the following way:
        #reverse = resvere + (num mod 10)
        #reverse*10,, num // 10
    while (num > 0):
        #Overflow! If Multiplying is greater than 2147483648 (2**31-1); then return 0
        digit = num % 10
        if (reverse > 214748364) or (reverse == 214748364 and digit > 7):
            return 0

        reverse = (reverse * 10) + (digit)
        num = num // 10

    #if number == negative,, then must remember sign!
    if negative_flag == True:
        reverse = 0 - reverse

    return reverse

x = 123
print(f"Original: {x}; Reverse: {reverse_integer(x)}")
x = -123
print(f"Original: {x}; Reverse: {reverse_integer(x)}")
x = 15681
print(f"Original: {x}; Reverse: {reverse_integer(x)}")
x = -1864
print(f"Original: {x}; Reverse: {reverse_integer(x)}")