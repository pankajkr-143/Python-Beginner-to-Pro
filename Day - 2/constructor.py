class Students:
    #default constructor
    def __init__(self, fullname, DoB, address):
        pass
    
    #parameterized constructor
    def __init__(self, fullname, DoB, address):
        self.name = fullname
        self.dob = DoB
        self.address = address
        print("adding new students in Database..")
        
        
s1 = Students("Macky", "25/08/2003", "Bhopal")
print("Name:", s1.name)   
print("Date of Birth:",s1.dob)
print("Address:",s1.address)
