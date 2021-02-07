class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        must_move=0
        for i,h in enumerate(sorted_heights):
            if h!=heights[i]:
                must_move+=1
        return must_move