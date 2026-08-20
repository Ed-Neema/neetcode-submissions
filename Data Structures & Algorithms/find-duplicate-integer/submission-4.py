class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0] * 10001
        for num in nums:
            count = arr[num]
            if count > 0:
                return num
            else:
                arr[num] += 1