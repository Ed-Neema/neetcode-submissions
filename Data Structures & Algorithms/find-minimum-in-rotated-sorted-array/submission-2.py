class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while nums[l] > nums[r]:
            removed = nums.pop(0)
            nums.append(removed)
        return nums[0]
