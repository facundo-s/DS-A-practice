class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        smallest=1
        for n in nums:
            if n<smallest:
                continue
            elif n==smallest:
                smallest+=1
            else:
                return smallest
        return smallest
        
#         smallest_pos_in_list=2**31 - 1
#         for n in nums:
#             if n<1:
#                 continue
#             elif n < smallest_pos_in_list:
#                 smallest_pos_in_list=n
        
#         if smallest_pos_in_list>1:
#             return 1
        
        
#         return smallest_pos_in_list
        
