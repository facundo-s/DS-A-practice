class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count=0
        maxLen=0
        for r in rectangles:
            largest = min(r)
            if largest>maxLen:
                maxLen=largest
                count=1
            elif largest==maxLen:
                count+=1
        return count
