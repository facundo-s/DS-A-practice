class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height= 0
        for g in gain:
            current_height+=g
            if current_height>max_height:
                max_height=current_height
        return max_height