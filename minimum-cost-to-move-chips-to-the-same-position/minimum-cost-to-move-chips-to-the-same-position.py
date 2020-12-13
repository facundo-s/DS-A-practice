class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        
        """
        is_even=False
        even=0
        odd=0
        for elem in position:
            if is_even:
                even+=elem
            else:
                odd+=elem
            is_even=not is_even
            
        return min(even,odd)
        """
        even=0
        odd=0
        for pos in position:
            if pos%2==0:
                even+=1
            else:
                odd+=1
        return min(even,odd)
