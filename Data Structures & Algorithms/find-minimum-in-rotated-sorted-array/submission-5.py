class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l,r = 0, len(nums)-1

        while l<=r:
            #the array is already properly sorted, so just return the number at index 0
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l+r) // 2
            res = min (res, nums[m])
            #should we search to the left or to the right? Which sorted portion does the m belong to?
            if nums[m] >= nums[l]: 
                #part of the left sorted portion
                l = m + 1
            else:
                #right sorted portion
                r = m - 1
        return res



 