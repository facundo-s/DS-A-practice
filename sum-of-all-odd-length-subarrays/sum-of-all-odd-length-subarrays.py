class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # odd=1
        # total=0
        # while odd<len(arr):
        #     for e in arr:
        #         total+=e*((odd+1)//2)
        #     odd+=2
        # total+=sum(arr)#last iteration
        # return total
        
        total_sum=0
        odd=1
        while odd<=len(arr):
            base_i=0
            while len(arr)-base_i>=odd:
                total_sum+=sum(arr[base_i:base_i+odd])
                base_i+=1
            odd+=2
        return total_sum
