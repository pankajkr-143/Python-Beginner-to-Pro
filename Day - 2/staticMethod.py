class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    @staticmethod   
    def student():
        print("Macky")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hello", self.name, "your avg score is:", sum/3)
        
s1 = Student("Dhiraj,", [88,87,89])
s1.get_avg()

#if want to change name

s1.name = "Macky,"
s1.marks = [98,99,96]
s1.get_avg()
s1.student()