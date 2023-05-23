class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = [0]*len(candies)
        max_candies = 0
        
        for i in range(len(candies)):
            if candies[i] > max_candies:
                max_candies =+ candies[i]
                
            candies[i] += extraCandies
            
        for i in range(len(candies)):           
            if candies[i] >= max_candies:
                result[i] = True
            else:
                result[i] = False
                
        return result
        