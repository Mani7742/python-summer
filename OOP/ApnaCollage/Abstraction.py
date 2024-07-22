class Car:
# Encapsulation--> Wrapping data and functions into a single unit
    #Constractor
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def Start(self):
        self.acc = True # Abstraction --> Hiding the implemantation Details
        self.clutch = True # Abstraction --> Only show the essentional Details
        print("Car has started")

Car1 = Car()
Car1.Start()