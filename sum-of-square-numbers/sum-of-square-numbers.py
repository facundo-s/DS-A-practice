class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # a and b are both smaller than c
        # brute force you iterate from c down to 0 and c to 0 and you check all pairs
        # O(n2) time
        
        sqrt = math.sqrt(c)
        
        if sqrt%1==0:
            return True
        
        found = False
        for a in range(1, int(sqrt//1)+1):
            found = found or (math.sqrt(c-a**2)%1==0)
        return found
