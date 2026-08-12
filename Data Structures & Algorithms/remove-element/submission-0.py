class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i keeps track of the position for the next valid element
        i = 0
        
        for num in nums:
            # If the current number is NOT the value to remove
            if num != val:
                nums[i] = num
                i += 1
                
        # i naturally represents the total count of valid elements
        return i
                    


        