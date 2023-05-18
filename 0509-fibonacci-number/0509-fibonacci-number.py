class Solution:
    def fib(self, n: int) -> int:
        
        i = 2  # We start at i=2 as we assume the first value and second values as 0 and 1
        sequence = list()
    
        sequence.append(0)
        sequence.append(1)
        
        if n == 0:
            return 0
    
        while i < n:
            fn = sequence[i-1] + sequence[i-2]
        
            sequence.append(fn)
        
            i += 1
        
        return (sequence[-1] + sequence[-2])
        