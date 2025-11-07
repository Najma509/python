class student:
    def getData(self, rollno, name, course):
        self.rollno = rollno
        self.name = name
        self.course = course

    def displaystudent(self):
         print("Roll Number:",self.rollno)
         print("Name:",self.name)
         print("course:",self.course)
               
class Test(student):
    def getMarks(self,marks):
       self.marks=marks

    def displayMarks(self):
        print("Total Marks:",self.marks)

class Result(Test):
    def calculateGrade(self):
        if self.marks>480:self.grade = "Distinction"
        elif self.marks>360:
            self.grade = "First class"
        elif self.marks>240:
            self.grade = "Second class"
        elif self.grade == "Failed":
             print("Result:",self.grade)
        
r=int(input("Enter Roll Number:"))
n=input("Enter Name:")
c=input("Enter Course name:")
m=int(input("Enter Marks:"))
print("Result")
stud1=Result()
stud1.getData(r,n,c)
stud1.getMarks(m)
stud1.displaystudent()
stud1.displayMarks()
stud1.calculateGrade()
   

