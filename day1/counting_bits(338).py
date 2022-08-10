class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n + 1):
            lst.append(sum(map(int, str(bin(i)[2:]))))
        return lst
