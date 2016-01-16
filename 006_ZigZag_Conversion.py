import math
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        """
        Creates a pattern list like this:
        1   7 8      14
        2  6  9    13
        3 5   10 12
        4     11

        In the list we store the row number

        position 1 2 3 4 5 6 7 8 ...
        row num  0 1 2 3 4 3 2 0 ...

        Then zip the row num list with the string, collect the chars into a list
        of rows, indexed by the row number

        output = [
          "1 7 8 14", # row 1
          "2 6 9 13", # row 2
          ...
        ]

        """
        pattern = range(0,numRows) #first down col, "zig"
        pattern += range(numRows-2, 0,-1) #diagnol "zag"
        repeats = len(s) / len(pattern) + 1
        char_pos = zip(s, pattern * repeats)
        rows = [""] * numRows
        for char in char_pos:
            rows[char[1]] += char[0]

        output = ""
        for row in rows:
            output += row

        return output
