class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        In this exercise I learned about poisitional arguments. They are arguments passed into functions by their position. A non-posiontal argument is passed with the form keyword = value. Python sort takes in non-positional arguments list.sort(reverse=True|False, key=myFunc)
        
        Review how lambda functions are defined in python
        
        The sort function without arguments also sub-sorts the inner value. 
        
        This is a ranges type of problem
        
        list.pop() has an optional argument of the index to remove
        
        trips = [[2,1,5],[3,3,7]], capacity = 4
        
        """
#         timestamp = []
#         for trip in trips:
#             timestamp.append([trip[1], trip[0]])
#             timestamp.append([trip[2], -trip[0]])

#         timestamp.sort()

#         used_capacity = 0
#         print(timestamp)
#         for time, passenger_change in timestamp:
#             used_capacity += passenger_change
#             if used_capacity > capacity:
#                 return False

#         return True
        timestamp = []
        for trip in trips:
            timestamp.append([trip[1],trip[0]])
            timestamp.append([trip[2], -trip[0]])
        
        timestamp.sort()
        
        for time in timestamp:
            capacity -= time[1]
            if capacity<0:
                print(time)
                return False
        return True
        
#         trips.sort(key=lambda x: x[1])
        
#         stack = []
        
#         for trip in trips:
#             capacity -= trip[0]
#             if stack:
#                 while stack[-1][2]<trip[1]:
#                     last = stack.pop()
#                     capacity+=last[0]
            
#             if capacity<0:
#                 return False
            
#             stack.append(trip)
#             stack.sort(key=lambda x: x[2])
            
        
#         return capacity>=0