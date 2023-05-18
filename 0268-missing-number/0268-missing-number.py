class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        r = range(len(nums))
        d = {}
        
        for i in nums:
            d[i] = i
            
        print(d)
            
        for i in r:
            if (i not in d):
                return i
            
        return len(nums)

        