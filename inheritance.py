class Person:
    def __init__(self) :
        self.name = input("\nEnter the name : ")
        self.age = int(input("Enter the age : "))
        self.gender = input("Enter the gender : ")

class Student(Person):
    def Student_info(self) :
        self.__init__()
        self.enrollment_no = str(input("Enter the Enrollment_Number : "))
        self.year = int(input("In which year you was studing : "))
        self.CGPA = float(input("Enter the CGPA : "))
        
    def finding_eligibility(self) :
        if(self.year <= 4 and self.year >= 2) and (self.CGPA >= 7.5 and self.CGPA <= 10.0) :
            print(self.year," YEAR STUDENT,",self.CGPA," IS PERFECT SO YOU'RE ELIGIBLE....! ")
        else :
            print(self.year," YEAR STUDENT ",self.CGPA, " YOU'RE NOT ELIGIBLE...! BETTER LUCK NEXT TIME")

class Faculty(Person):
    def Faculty_info(self) :
        self.__init__()
        self.department = input("Enter the Department : ")
        self.PU_staff = input("Are you PU staff Or Not : ")

    def PU_acess(self) :
        if(self.PU_staff == 'Yes'):
            print(self.name," from " ,self.department ," PU_staff Is Accessing The System....!")
        elif(self.PU_staff == 'No') :
            print(self.name," from " ,self.department ,"Non- PU staff So Limited access...!")
            print("You Can Manipulate Students Data")
        else :
            print("Please Enter Yes Or NO")

print("------- Parul System ManageMent -------")
print("1. Faculty\n2. Student\n3. Exit")

choice = int(input("Enter Your Choice(1-3): "))

while True :
    if(choice == 1) :
        print("---- FACULTY ----")
        faculty = Faculty()
        faculty.Faculty_info()
        faculty.PU_acess()
        break

    elif(choice == 2) :
        print("---- STUDENT ----")
        stu = Student()
        stu.Student_info()
        stu.finding_eligibility()
        break

    elif(choice == 3):
        print("Exiting From The System\nPlease Turn Off The System Properly...!")
        break

    else :
        print("Invalid choice\nPlease Pick Between(1-3)")
        break

print("\nThankYou For Logging Into PU's System\n")
