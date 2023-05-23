class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = [0]*len(candies)
        max_candies = max(candies)
            
        for i in range(len(candies)):
            candies[i] += extraCandies
                
            if candies[i] >= max_candies:
                result[i] = True
            else:
                result[i] = False
                
        return result
        