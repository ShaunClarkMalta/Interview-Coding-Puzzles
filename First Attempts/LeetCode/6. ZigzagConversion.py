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

''' Input: Word, Rows
- Counter starting at 0
Add Letter to Row, Increments Counter
if counter = row_length-1, then go in reverse order
'''

#Purely to see how best I can recreate the pattern via nested lists
'''def test_array_print():
    row1 = [1.1, 1.2, 1.3, 1.4, 1.5]
    row2 = [2.1, 2.2, 2.3, 2.4, 2.5]
    row3 = [3.1, 3.2, 3.3, 3.4, 3.5]

    test = [row1, row2, row3]
    for rows in test:
        print(rows)

test_array_print()'''

def zigzag_conversion(word, number_rows):
    counter = 0
    reverse = False
    rows = []
    result = []

    #Create necessary rows based on 'number_rows'
    for i in range(number_rows):
        rows.append([])

    #if len(word) == 1; return word
    if (len(word) == 1) or (number_rows == 1):
        return word
    
    #Iterate through letters, assigning each to the end of the appropriate row
    for letter in word:
        rows[counter].append(letter)

        #Check limits to change direction. If counter == 0, must increment and reverse = False. If counter == len(word)-1, decrement and reverse = True 
        if counter == 0:
            reverse = False
            counter += 1

        elif counter == (number_rows-1):
            reverse = True
            counter -= 1

        else:
            if reverse == False:
                counter += 1
            else:
                counter -= 1

    for row in rows:
        for element in row:
            result.append(element)

    return "".join(result)

word = "PAYPALISHIRING"
rows = 3
print(f"{word} in {rows} rows: {zigzag_conversion(word, rows)}")
rows = 4
print(f"{word} in {rows} rows: {zigzag_conversion(word, rows)}")
word = "A"
rows = 1
print(f"{word} in {rows} rows: {zigzag_conversion(word, rows)}")

#Future improvement could be to actually print the Word in the Zigzag pattern