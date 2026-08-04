class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i, val in enumerate(temperatures):            
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > val:
                    result[i] = j - i
                    break                
        return result


        