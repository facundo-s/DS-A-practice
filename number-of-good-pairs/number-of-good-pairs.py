class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs=0
        
        for i in range(len(nums)):
            j=i+1
            if j==len(nums):
                break
            for k in range(j, len(nums)):
                if nums[i]==nums[k]:
                    good_pairs+=1
        
        return good_pairs
