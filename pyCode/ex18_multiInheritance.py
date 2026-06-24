class Teacher:
    def printJob(self):
        print("Teaches Math")

class youtuber:
    def printJob(self):
        print("Creates YouTube content")

class Student(Teacher,youtuber):
    def printJob(self):
        print("Learns Math")
        Teacher.printJob(self)
        youtuber.printJob(self)


s = Student()
s.printJob()