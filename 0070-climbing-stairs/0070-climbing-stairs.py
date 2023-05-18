class Solution:
    def climbStairs(self, n: int) -> int:
        
        sequence = [1, 2]
        i = 2
        
        if n == 1:
            return 1
        
        while i < n:
            fn = sequence[i-1] + sequence[i-2]          
            sequence.append(fn)
            i += 1
            
        return sequence[-1]