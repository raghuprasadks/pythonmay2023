# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        # YOUR CODE STARTS HERE
        msg = f'{self.cid}({self.credits}): {self.cname}'
        #print(msg)
        return msg

    __repr__ = __str__

    def __eq__(self, other):
        # YOUR CODE STARTS HERE
        #pass
        if isinstance(other,Course):
            if self.cid==other.cid:
                return True
            else:
                return False
        else:
            return False


class Catalog:
    '''
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        # YOUR CODE STARTS HERE
        #pass
        self.courseOfferings={}
        #courseOfferings

    def addCourse(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        #pass
        course=Course(cid,cname,credits)
        if cid not in self.courseOfferings.keys():
            self.courseOfferings[cid]=course
            return "Course added successfully"
        else:
            return "Course already added"

    def removeCourse(self, cid):
        # YOUR CODE STARTS HERE
        #pass
        if cid in self.courseOfferings.keys():
            self.courseOfferings.pop(cid)
            return "Course removed successfully"
        else:
            return "Course not found"


    def _loadCatalog(self, file):
        with open(file, "r") as f:
            course_info = f.read()
        #print("data type of course_info")
        #print(type(course_info))
        couselist = course_info.split('\n')
        #print(type(couselist))
        print("course list")
        print(couselist)
        for course in couselist:
            courseaftersplit = course.split(',')
            cid = courseaftersplit[0]
            cname = courseaftersplit[1]
            credits = courseaftersplit[2]

            course = Course(cid, cname, credits)
            self.courseOfferings[cid] = course
            #print("course after split 0 ",courseaftersplit[0])
            #print("course after split 1 ", courseaftersplit[1])
            #print("course after split 2 ", courseaftersplit[2])
            #self.addCourse(courseaftersplit[0],courseaftersplit[1],courseaftersplit[2])
            #print("course offerings")
        print(self.courseOfferings)
        # YOUR CODE STARTS HERE


def run_tests():
    import doctest

    # Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Course with the name of the function you want to test
    #doctest.run_docstring_examples(Course, globals(), name='HW2',verbose=True)
    doctest.run_docstring_examples(Catalog, globals(), name='HW2', verbose=True)


if __name__ == "__main__":
    run_tests()