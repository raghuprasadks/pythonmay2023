class Instructor():
    name: str=''
    courses: list=[]

    def __init__(self,_name):
        self.name = _name

    def getName(self):
        return self.name

    def setName(self,_name):
        self.name = _name

    def getCourse(self):
        return self.courses

    def removeCourse(self,_course):
        #pass
        self.courses.remove(_course)

    def addCourse(self,course):
        self.courses.append(course)

instructor1 = Instructor("raghu")
print(instructor1.getName())
instructor1.addCourse("Python")
instructor1.addCourse("ML")
instructor1.addCourse("Web Development")
print(instructor1.getCourse())
print(instructor1.removeCourse("ML"))
print("after removal ")
print(instructor1.getCourse())



