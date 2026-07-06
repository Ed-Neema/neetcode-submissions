class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for index,number in enumerate(nums):
            product = 1
            for idx, value in enumerate(nums):
                if(idx==index):
                    continue
                else:
                    product=product*value
            output.append(product)
        return output
        