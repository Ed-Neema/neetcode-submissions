class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #we set  r to max value in pile because we know that this is the highest eating rate possible
        res = r # since we are looking for the minimum, we can set it to the max rate that we know will work. 

        while l <= r:
            k = (l+r)//2
            #then compute, for this rate, how many hours does it take to eat all bananas
            hours = 0
            for p in piles:
                hours+= math.ceil(p/k)
            if hours <= h:
                #update result to new minimum
                res = min(k, res)
                r = k - 1 #search the left portion to see if there's an even smaller possible value
            else: #if we took more time than the max amount of time we have, our k was too small, we need a larger 
                l = k + 1 #set it to the right of k
        
        return res

