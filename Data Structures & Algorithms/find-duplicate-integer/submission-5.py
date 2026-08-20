class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # arr = [0] * 10001 #had to add 1 so that the array is able to store value for index 10,000
        arr = [0] * len(nums)
        for num in nums:
            count = arr[num]
            if count > 0:
                return num
            else:
                arr[num] += 1