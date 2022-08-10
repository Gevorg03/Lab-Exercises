class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n)[2:])
        s = "0" * (32 - len(s)) + s
        sum, degree = 0, 0
        for el in s:
            sum += int(el) * (2 ** degree)
            degree += 1
        return sum
