class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        my_dict = dict()
        
        for i in range(len(nums)):
            if (nums[i] in my_dict) and ((i - my_dict[nums[i]]) <= k):
                return True
            else:
                my_dict[nums[i]] = i
        return False
        