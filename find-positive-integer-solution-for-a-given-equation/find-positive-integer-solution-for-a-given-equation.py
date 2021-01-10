"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""
​
class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        solutions=[]
        x,y=1,1
        
        while x<1000 and y<1000:
            func_output = customfunction.f(x,y)
            
            if func_output==z:
                solutions.append([x,y])
            if func_output>z and y==1:
                break
            elif func_output>z or y+1>1000:
                x+=1
                y=1
                continue
            y+=1
            
        return solutions
                
                
                
                
                
                
                
