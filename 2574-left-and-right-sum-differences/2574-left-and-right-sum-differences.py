class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        answer = [0]*len(nums)
        leftSum = []
        rightSum = []
        
        previous_sum = 0
        total_sum = sum(nums)
        
        for i in range(len(nums)):
            leftSum.append(previous_sum)
            previous_sum += nums[i]
            
            total_sum -= nums[i]
            rightSum.append(total_sum)
        
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        return answer
        