'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.'''

'''
Dictionary with Symbols : Value
Total counter = 0
Start from right -> left
If next is smaller, then need to subtract'''

roman_dictionary = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

def roman_conv(roman_string):
    current_value = 0                                   #For using the Current value
    total = 0                                           #Keeps track of totals
    should_add = True                                   #Shows whether to add or subtract next value
    roman_string = roman_string[::-1]                   #Ensures string is capitalized. Will go in reverse order

    for i, symbol in enumerate(roman_string):           #Parses through the symbols, one by one
        current_value = roman_dictionary[symbol]
        if (i < len(roman_string) - 1):
            if should_add == False:                     #If Should_Add is False, then we should adjust current_value by subtracting
                counter -= current_value
                if roman_dictionary[roman_string[i]] < roman_dictionary[roman_string[i+1]]:     #If the next symbol has a higher value, then we can stop calculating the segment and have to go back to adding
                    total += counter
                    should_add = True
                else:                                       #Otherwise, we can continue 
                    pass
            else:
                if roman_dictionary[roman_string[i]] > roman_dictionary[roman_string[i+1]]:     #If the next symbol has a lower value, then we know that the next steps will be subtracting
                    counter = current_value                 #Create a 'bucket' for this segment
                    should_add = False                      #Raise Flag for subtraction
                else:
                    total += current_value
        else:                                               #Final step when reching the end of the string
            if should_add:
                total += current_value
            else: 
                total = total + counter - current_value
    return total

test1 = "MCMXCIV"
test2 = "LXI"
test3 = "XLVII"
test4 = "MMMCMXCIX"
test5 = "CDXLIV"
test6 = "DCCCXC"
test7 = "XCIX"
print(f"Roman: {test1} - Decimal: {roman_conv(test1)}")
print(f"Roman: {test2} - Decimal: {roman_conv(test2)}")
print(f"Roman: {test3} - Decimal: {roman_conv(test3)}")
print(f"Roman: {test4} - Decimal: {roman_conv(test4)}")
print(f"Roman: {test5} - Decimal: {roman_conv(test5)}")
print(f"Roman: {test6} - Decimal: {roman_conv(test6)}")
print(f"Roman: {test7} - Decimal: {roman_conv(test7)}")