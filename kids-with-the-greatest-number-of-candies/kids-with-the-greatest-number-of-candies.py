class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = max(candies)
        
        return [x+extraCandies>=greatest for x in candies]
        
