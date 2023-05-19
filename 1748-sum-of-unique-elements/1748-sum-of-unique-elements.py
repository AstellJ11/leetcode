class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        d = {}
        total = 0
        
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
                
        for key, value in d.items():
            if value == 1:
                total += key
                                
        return total
        