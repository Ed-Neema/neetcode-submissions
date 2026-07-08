class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1=0
        p2=len(s)-1
        if(len(s)==0 or len(s)==1):
            return True

        while (p2 > p1):
            while p1 < p2 and not(s[p1].isalnum()):
                if(p1<len(s)-1):
                    p1+=1
            while p1 < p2 and not(s[p2].isalnum()):
                if(p2>0):
                    p2-=1
            if(s[p1].lower()== s[p2].lower()):
                p1+=1
                p2-=1
            else:
                return False
        return True