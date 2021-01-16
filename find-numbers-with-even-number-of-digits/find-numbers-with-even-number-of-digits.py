class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number_of_even=0
        for n in nums:
            digits=0
            while n>0:
                n=n//10
                digits+=1
            if digits%2==0:
                number_of_even+=1
        return number_of_even
