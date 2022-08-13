"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        same = ''
        min_element = min(strs, key=len)
        strs.remove(min_element)
        for i in range(len(min_element)):
            l = min_element[i]
            count = 0
            for el in strs:
                if l == el[i]:
                    count += 1
            if count == len(strs):
                same += l
            else:
                return same
        return same
