class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        answer = [0]*len(nums)
        
        previous_sum = 0
        max_sum = sum(nums)
        
        for i in range(len(nums)):
            leftSum = previous_sum
            previous_sum += nums[i]
            
            max_sum -= nums[i]
            rightSum = max_sum
        
            answer[i] = abs(leftSum - rightSum)
        
        return answer
        