class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        sequence = range(1, n+1)
        
        for i in sequence:
            if (i % 3 == 0) & (i % 5 == 0):
                answer.append("FizzBuzz")
            elif (i % 3 == 0):
                answer.append("Fizz")
            elif (i % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
                
        return answer
            
            
        