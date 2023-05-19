class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewels_dict = {}
        total = 0
        
        for char in jewels:
            if char not in jewels_dict:
                jewels_dict[char] = 1
            else:
                jewels_dict[char] += 1
        
        for char in stones:
            if char in jewels_dict:
                total += 1
            
        return total
        