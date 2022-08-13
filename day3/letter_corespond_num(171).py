"""Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number."""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        index = 0
        for el in columnTitle:
            index = index * 26 + (ord(el) - 64)
        return index
