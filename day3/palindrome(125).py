"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.  Given a string s, return true if it is a palindrome, or false otherwise."""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "")
        s = s.lower()
        print(s)
        if s == s[::-1]:
            return True
        return False
        
