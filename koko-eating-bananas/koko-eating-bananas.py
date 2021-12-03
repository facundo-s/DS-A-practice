class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # calculate whether a value K is possible to finish within time
        def canFinish(K):
            total = 0
            for i,n in enumerate(piles):
                total += floor(n/K)
                if n%K>0:
                    total+=1
            return total<=h
        
        # iterate from 1 forward to find the smallest K that satisfies
        # iteration is linear time, which is not fast enough
        # counter = 1
        # while counter<=max(piles):
        #     if canFinish(counter)==True:
        #         return counter
        #     counter+=1
        
        # solve bin search [1 ... 30]
        # find the first one that can solve
        lo, hi = 1, max(piles)
        while lo<hi:
            mi = floor((lo+hi)/2)
            if not canFinish(mi):
                lo=mi+1
            else:
                hi=mi
        return lo
    
            
            
            
            
            
            
            