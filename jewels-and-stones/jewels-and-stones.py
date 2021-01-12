class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=set(list(jewels))
        count = 0
        for s in stones:
            if s in jewels:
                count+=1
                
        return count
