class Member:
    college = 'XYZ'
    def full_name(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print(f"full name is {fname} {lname}")
class Student(Member):
    def student_info(self):
        print(self.college)
    def student_fullname(self):
        print(f"student full name is {self.fname} {self.lname}")

s1 = Student()

s1.student_info()
s1.college = 'ABC'
s1.student_info()
s1.full_name('Prasanth','Neel')
s1.student_fullname()
s1.fname = 'Rahul'
s1.lname = 'Dravid'
s1.student_fullname()