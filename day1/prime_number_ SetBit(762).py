class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(num):
            return all([(num % i) for i in range(2, int(num**0.5) + 1)]) and num > 1
        
        count = 0
        for i in range(left, right + 1):
            i = str(bin(i)[2:])
            if is_prime(i.count("1")):
                count += 1
        return count  
