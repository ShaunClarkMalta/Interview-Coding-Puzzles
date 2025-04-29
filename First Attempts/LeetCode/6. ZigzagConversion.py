'''Zigzag Conversion
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''
#Purely to see how best I can recreate the pattern via nested lists
def test_array_print():
    row1 = [1.1, "", 1.3, 1.4, 1.5]
    row2 = [2.1, 2.2, 2.3, 2.4, 2.5]
    row3 = [3.1, 3.2, 3.3, 3.4, 3.5]

    test = [row1, row2, row3]
    for rows in test:
        print(rows)

word = "example"
rows = 5
test_array_print()