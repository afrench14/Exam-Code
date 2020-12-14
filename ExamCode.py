#code to create a bird class and Duck and Canary child classes

#instanciate the mother class
class Bird:
    #constructor
    def __init__(self, birdName, petType):
        #adding attributes
        self.Name = input("what is the birds name?: ")
        self.Lifespan = 10
        self.Age = 0
        self.Dead = False
    
    #adding methods
    #method to return sound
    def MakeSound(self):
        if self.Dead == True:
            print("bird is dead")
            pass
        return("chirp")
    #method to return age
    def GetAge(self):
        if self.Dead == True:
            print("bird is dead")
            pass
        return(self.Age)
        if self.Age >= self.Lifespan:
            return("so sorry, but this bird is dead as it grew too old")
            self.Dead = True
    #method to increase age:
    def GrowOld(self):
        if self.Dead == True:
            print("bird is dead")
            pass
        self.Age =+ 1
    #method to return name
    def GetName(self):
        if self.Dead == True:
            print("bird is dead")
            pass
        print("this birds name is", self.Name)



#instanciate a first child class
class Canary(Bird):

    #this inherits the constructors and methods from the parent class
    #so we only need to override the method inside the child class
    def(super(MakeSound)):





#driver code
NewBird = Bird()
NewCanary = Canary()