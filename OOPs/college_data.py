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
    # def __init__(self,salary):
    #     self.salary = salary
    def GetSalary(self,salary):
        print(f"your salary is {salary}")
    def teaching_course(self):
        print(f"Your course is {self.course} ")
    def address_faculty(self):
        print(f'your adddress is {self.address}')

class Student(Member):
    # def __init__(self,fee):
    #     self.fee = fee

    def course_fee(self,fee):
        print(f"your course fee is {fee} and fullname is {self.firstname+self.lastname}")
faculty1 = Faculty('prasanth','Neel','n@gmail.com','00034','Bangalore','python',123345,'12-12-2025')
faculty1.fullname()
faculty1.address_faculty()
faculty1.teaching_course()