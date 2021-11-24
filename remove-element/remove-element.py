class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        nums = [1,2,3], val = 1
        
        first iteration -> nums=[1,2,3], val=1, pointer=0
        second iteration -> nums=[2,2,3], val=1, pointer=1
        third iteration -> nums=[2,3,3], val=1, pointer=2
        """
        
        pointer = 0
        for i, n in enumerate(nums):
            if n == val:
                continue
            nums[pointer]=n
            pointer += 1
            
        return pointer