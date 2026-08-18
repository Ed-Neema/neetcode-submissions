class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for num in nums2:
            # 1. Pass 'm' to only search the valid sorted portion of the array
            position = self.binary_search(nums1, m, num)
            
            # 2. Insert into nums1
            nums1.insert(position, num)
            
            # 3. Drop a placeholder zero. Because we inserted an item, 
            # the original trailing zeros are shifted. The first available zero 
            # is now sitting exactly at index (m + 1).
            nums1.pop(m + 1)
            # nums1.pop()
            
            # 4. Increment m because nums1 now holds one more valid, sorted number
            m += 1
        
    
    def binary_search(self, arr, current_m, target):
        # 5. Restrict the boundaries to only search the current valid elements
        l, r = 0, current_m - 1
        
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l