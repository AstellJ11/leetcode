class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # slow method: loop index starting at 0
        # speed up using len/2 as starting true
        
        left_sum = 0
        right_sum = sum(nums)  # 28
        
        for i in range(len(nums)):
            right_sum = right_sum - nums[i]
            
            if left_sum == right_sum:
                return i
            
            left_sum = left_sum + nums[i]
            
        return -1
            
            
        