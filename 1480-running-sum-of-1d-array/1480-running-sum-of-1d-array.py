class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        running_sum = list()
        previous_sum = 0
        
        for i in range(len(nums)):
            current_sum = nums[i]     
            running_sum.append(previous_sum + current_sum)
            previous_sum = previous_sum + current_sum
        
        return running_sum