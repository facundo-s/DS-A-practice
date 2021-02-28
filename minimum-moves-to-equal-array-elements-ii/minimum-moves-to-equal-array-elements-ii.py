class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # O(nlogn) runtime O(n) space, both from sort
        mean = sorted(nums)[len(nums)//2]#sum(nums)//len(nums)
        steps = 0
        for n in nums:
            steps += abs(mean-n)
        return steps