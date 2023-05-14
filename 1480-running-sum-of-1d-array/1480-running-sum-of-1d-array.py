class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        running_sum = list()
        previous_sum = 0
        
        for i in range(len(nums)):    
            running_sum.append(previous_sum + nums[i])
            previous_sum = previous_sum + nums[i]
        
        return running_sum