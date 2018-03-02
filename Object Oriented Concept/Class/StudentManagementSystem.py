#
class PersonInfo :
    def __init__(self,name="",age=0,address="",dob=""):
        self.name=name
        self.age=age
        self.address=address
        self.dob=dob
    def __del__(self):
        del(self)

class Student(PersonInfo):
    def __init__(self,rollNo,percentage=0.0):
        self.rollNo=rollNo
        self.percentage=percentage
    def __del__(self):
        del (self)

class Teacher(PersonInfo):
    def __init__(self,eId=0,salary=0.0):
        self.eId=eId
        self.salary=salary
    def __del__(self):
        del(self)
class Cource :
    def __init__(self,cNo=0,cName=""):
        self.cNo=cNo
        self.cName=cName
    def __del__(self):
        del(self)
class StudentManager :
    def __init__(self):
        self.studentsList=[]
        self.courcesList=[]
    def __del__(self):
        del(self.studentsList)
        del(self.courcesList)
def main():

if __name__=="__main__":
    main()