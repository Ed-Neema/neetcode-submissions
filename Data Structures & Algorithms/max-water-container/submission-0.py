class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        for p1,value in enumerate(heights):
            p2=len(heights)-1
            while p2>p1:
                currentAmount = (p2-p1) * min(value,heights[p2])
                maxAmount = max(maxAmount,currentAmount)
                p2-=1
        return maxAmount
