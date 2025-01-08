class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letter ={
            'A' : 1,
            'B' : 2,
            'C' : 3,
            'D' : 4,
            'E' : 5,
            'F' : 6,
            'G' : 7,
            'H' : 8,
            'I' : 9,
            'J' : 10,
            'K' : 11,
            'L' : 12,
            'M' : 13,
            'N' : 14,
            'O' : 15,
            'P' : 16,
            'Q' : 17,
            'R' : 18,
            'S' : 19,
            'T' : 20,
            'U' : 21,
            'V' : 22,
            'W' : 23,
            'X' : 24,
            'Y' : 25,
            'Z' : 26
        }
        column = 0
        for title in columnTitle:
            value = letter[title]
            column = column * 26 + value
        return column 

# Alternative

def titleToNumber(columnTitle):
    result = 0
    for char in columnTitle:
        value = (ord(char) - 64) + 1  
        result = result * 26 + value  
    return result

# Test cases
print(titleToNumber("A"))   # Output: 1
print(titleToNumber("Z"))   # Output: 26
print(titleToNumber("AA"))  # Output: 27
print(titleToNumber("AB"))  # Output: 28
print(titleToNumber("ZY"))  # Output: 701
