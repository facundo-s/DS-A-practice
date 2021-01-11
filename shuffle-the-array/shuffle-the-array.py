class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        #find its index in the first half or second half
        #if it's in first half its new index is 2*i+1
        #second half is 2*i
        
        #there's a better data way than this
        shuffled = [None]*2*n
        for i in range(2*n):
            if i<n:
                shuffled[2*i]=nums[i]
            else:
                shuffled[2*(i-n)+1]=nums[i]
                
        return shuffled
        
        
