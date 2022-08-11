class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums.count(nums[count]) > 1:
                del nums[nums.index(nums[count])]
            else:
                count += 1
        return len(nums)  
