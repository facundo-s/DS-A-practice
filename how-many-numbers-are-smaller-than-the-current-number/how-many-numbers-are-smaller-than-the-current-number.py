class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rl=nums.copy()
        nums.sort()
        for i in range(len(nums)):
            rl[i]=nums.index(rl[i])
        return rl
