class Student:
    def __init__(self, name):
        self.name = name
        
s1 = Student("Macky")
print(s1.name)
del s1.name
print(s1.name)



#there is an error 
#it will be printed Name but show an error there 
#Macky
#Traceback (most recent call last):
  #File "c:\Users\kumar\OneDrive\Desktop\Python Coding\Day - 4\delKey.py", line 8, in <module>
   # print(s1.name)
    #      ^^^^^^^
#AttributeError: 'Student' object has no attribute 'name'