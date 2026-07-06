class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        product = 1
        zero_present = False
        zero_count = 0;
        for i in nums:
            if(i==0):
                zero_present = True
                zero_count+=1
                continue
            else:
                product = product * i
        for index,value in enumerate(nums):
            if(value == 0 and zero_count > 1):
                output[index] = 0
            elif(value == 0 and zero_count==1):
                output[index] = product
            elif(zero_present == True):
                output[index] = 0
            else:
                output[index] = int(product/nums[index])
        return output
        