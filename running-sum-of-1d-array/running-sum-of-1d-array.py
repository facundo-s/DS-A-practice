class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs_nums = [None]*len(nums)
        for i in range(len(nums)):
            rs_nums[i]=sum(nums[:i+1])
        return rs_nums
