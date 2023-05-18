class Solution:
    def tribonacci(self, n: int) -> int:
        
        sequence = [0, 1, 1]
        i = 3
        
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        
        while i < n:
            fn = sequence[i-1] + sequence[i-2] + sequence[i-3]
        
            sequence.append(fn)
        
            i += 1
        
        return (sequence[-1] + sequence[-2] + sequence[-3])
            
        