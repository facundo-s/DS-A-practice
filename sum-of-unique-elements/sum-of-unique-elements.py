class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        frequencies = [0]*101
        for n in nums:
            frequencies[n]+=1
        unique_sum=0
        for i, f in enumerate(frequencies):
            if f==1:
                unique_sum+=i
        
        return unique_sum
        