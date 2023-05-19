class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        x = 0        
        d = {"++X" : 1, "X++" : 1, "--X" : -1, "X--" : -1}
        
        for i in operations:   
            if i in d:
                x += d.get(i)
        
        return x