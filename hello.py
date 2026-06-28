# class LeapYear :
#     def checkL(year):
#         if((year % 4 == 0) and(year % 400 == 0)):
#             print("Leap Year")
#         else :
#             print("Not a Leap Year")

# year = int(input("Enter the year: "))
# ye = LeapYear
# ye.checkL(year)

def factorial(Number):
    fact = 1
    for i in range(Number,1,-1):
        fact *= i
    print(fact)

Number = int(input("Enter the NUmber :"))
factorial(Number)



class Student1 :
    def __init__(self,name,cgpa) :
        self.name = "SHANMUKHA"
        self.cgpa = 8.06

class Parents :
    def __init__(self,name,Occupasion,FeePaid):
        self.name = "SRINIVAS"
        self.Occupasion = "Teacher"
        self.FeePaid = 500,000
    
class info(Student1) :
    def __init__(self) :
        print("This Info Is Related to ",self.name):

y = info()
y.info()


