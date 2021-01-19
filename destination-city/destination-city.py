class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        current = paths[0][0]
        
        while True:
            nc = Solution.nextCity(current, paths)
            if nc==None:
                return current
            else:
                current=nc
        
    def nextCity(source: str, paths: List[List[str]]):
        for path in paths:
            if path[0]==source:
                return path[1]
        return None
