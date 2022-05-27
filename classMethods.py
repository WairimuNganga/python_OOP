#Class Methods are uswd to define the behaiour of an object.
#This are defined as functions inside the class.
#The first argument of a class method is always self.
class Students:
    school = "AkiraChix"
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country 

    def greet(self):
        return f"Hello {self.name} from {self.country},welcome to {self.school}"