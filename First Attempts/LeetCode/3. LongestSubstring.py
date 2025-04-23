'''Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

'''Input String
Parse string character by character
if i = i+1; then break
return count of string'''

def find_substring(s):
    substring = ""
    substring_set = set()
    maximum_length = 0

    for char in s:
        #if the character is the same as the previous character in the substring, then reset and go to the next 
        if substring and (char in substring_set):
            substring = ""
            substring_set = set()
        #Otherwise, increment the substring
        else:
            substring += char
            substring_set.add(char)

        #Before proceeding, check if new maximum length 
        if len(substring_set) > maximum_length:
            maximum_length = len(substring_set)
    
    return maximum_length

s = "abcabcbb"
print(f"The Maximum Substring length of {s} is: {find_substring(s)}")

s = "bbbbb"
print(f"The Maximum Substring length of {s} is: {find_substring(s)}")

s = "pwwkew"
print(f"The Maximum Substring length of {s} is: {find_substring(s)}")