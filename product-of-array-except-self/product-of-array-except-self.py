class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        You can multiply all elements in an array with math.prod
        
        """
        output = [None]*len(nums)
        output[0]=1
        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]
        
        R = 1
        for i in reversed(range(len(nums))):
            output[i]=output[i]*R
            R*=nums[i]
        
        return output
        
        """
        # here is my brute force approach with O(n2) runtime
        
        output = [None]*len(nums)
        for i in range(len(nums)):
            output[i]=math.prod(nums[:i]+nums[i+1:])
            
        return output
        """
        