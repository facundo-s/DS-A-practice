class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        last = float("-inf")
        for i, a in enumerate(arr):
            if a>last:
                last=a
                continue
            return i-1
        # last, peak_i, up = None, None, True
        # for i, a in enumerate(arr):
        #     if up:
        #         if a>last:
        #             last = a
        #             continue
        #         last=a
        #         peak_i=i
        #         up=False
        #         continue
        #     else:
        #         if a<last:
        #             last=a
        #             continue
        #         return False
        # if peak_i==None:
        #     return 