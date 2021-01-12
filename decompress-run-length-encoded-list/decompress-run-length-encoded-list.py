class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        r_list=[]
        for i in range(len(nums)//2):
            r_list+=[nums[2*i+1]]*nums[2*i]
        return r_list
