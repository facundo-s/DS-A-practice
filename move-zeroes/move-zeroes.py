class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """  
       
        i = 0
        num_zeros = 0
        
        while i<len(nums):
            if nums[i]==0:
                num_zeros+=1
            elif num_zeros > 0:
                nums[i-num_zeros]=nums[i]
                nums[i]=0
            i+=1
        
                
