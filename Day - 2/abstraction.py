#eaxmple a car

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start (self):
        self.clutch = True
        self.acc = True
        print("Car started...")
        
    def exception(self):
        self.brk = True
        print("Put the break button then")
        
    def stop(self):
        self.brk = True
        print("Car Stopped.")
        
car1 = Car()
car1.start()
car1.exception()
car1.stop()