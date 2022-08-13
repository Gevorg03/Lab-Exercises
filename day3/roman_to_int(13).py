class Solution:
    def romanToInt(self, s: str) -> int:
        dict_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        dict_nums2 = {"CM": 900, "XC": 90, "IV": 4, "IX": 9, "XL": 40, "CD": 400}
        sum = 0
        i = 0
        while i < len(s):
            if s[i:i + 2] in dict_nums2:
                sum += dict_nums2[s[i:i + 2]]
                i += 1
            else:
                sum += dict_nums[s[i]]
            i += 1
        return sum   
