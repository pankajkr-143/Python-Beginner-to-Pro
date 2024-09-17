#Create students class taes name and marks of 3 subjects as arguments in constructor.
#Then create a method to print the average.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
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