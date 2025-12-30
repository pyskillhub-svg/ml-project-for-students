class Member:
    def __init__(self,firstname,lastname,email,memberId,address,course,mobileno,dateofjoin):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.memberId = memberId
        self.address = address
        self.mobileno = mobileno
        self.dateofjoin = dateofjoin
        self.course = course
    def fullname(self):
        print(self.firstname + self.lastname)
class Faculty(Member):
    def __init__(self,salary):
        self.salary = salary
    def GetSalary(self):
        print(f"your salary is {self.salary}")
    def teaching_course(self):
        print(f"Your course is{self.course} ")

class Student(Member):
    def __init__(self,fee):
        self.fee = fee

    def course_fee(self):
        print(f"your course fee is {self.fee} and fullname is {self.firstname+self.lastname}")
faculty1 = Faculty('Python')
faculty1.teaching_course()