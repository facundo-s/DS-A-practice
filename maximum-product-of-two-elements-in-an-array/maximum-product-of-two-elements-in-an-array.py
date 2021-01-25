class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=max(nums)
        nums.remove(a)
        return (max(nums)-1)*(a-1)
        
