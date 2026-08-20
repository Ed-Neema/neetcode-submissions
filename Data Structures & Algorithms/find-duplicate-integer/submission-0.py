class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        duplicate = 0
        for number in nums:
            count = hashmap.get(number, 0)
            if count != 0:
                duplicate = number
                return number
            hashmap[number] = count + 1  
        return  duplicate    