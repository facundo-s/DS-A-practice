class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        current=points[0]
        steps=0
        for target in points[1:]:
            x=target[0]-current[0]
            y=target[1]-current[1]
            steps+=max(abs(x),abs(y))
            current=target
        return steps
​
