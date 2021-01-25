class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance=0
        z=x^y
        tmp=1
        while tmp<=z:
            if tmp&z>0:
                distance+=1
            tmp=tmp<<1
            
        return distance
​
