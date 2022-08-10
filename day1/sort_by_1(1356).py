class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr = sorted(arr)
        for i in range(len(arr) - 1):
            for j in range(len(arr) - i - 1):
                num1 = bin(arr[j])[2:]
                num2 = bin(arr[j + 1])[2:]
                if str(num1).count("1") > str(num2).count("1"):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr 
