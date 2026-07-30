class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        mid = len(nums) // 2
        l , r = 0, len(nums) - 1
        while l <= r:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                mid = (l+r) // 2
            else:
                l = mid + 1
                mid = (l+r) // 2
        return -1

        