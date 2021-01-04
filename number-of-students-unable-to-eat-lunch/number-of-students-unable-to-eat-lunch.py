class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        i=7000
        while i>0:
            if students==sandwiches:
                return 0
            if students[0]==sandwiches[0]:
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
            else:
                a = students[0]
                students.remove(students[0])
                students.append(a)
            if students[0]!=sandwiches[0] and (sum(students)==len(students) or sum(students)==0):
                print(students, sandwiches)
                return len(students)
            print(students, sandwiches)
            i-=1
                
        
