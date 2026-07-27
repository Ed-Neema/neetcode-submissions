class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = [0,0] 
        #if list is empty
        if len(numbers) == 0:
            return []
        while l < r:
            summation = numbers[l] + numbers[r]
            if summation == target:
                res[0] = l + 1
                res[1] = r + 1
                break
            elif summation < target:
                l+=1
            else:
                r -= 1
        return res


        