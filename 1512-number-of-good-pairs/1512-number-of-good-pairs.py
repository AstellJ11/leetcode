class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        d = {}
        total = 0
        
        for i in range(len(nums)):
            if (nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
                
        for i in d.values():
            total += round(i * (i-1) / 2)
            
        return total
        