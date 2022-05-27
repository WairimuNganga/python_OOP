
# class Student:
#     name = "Effence"
#     age = 21
#     country = "Kenya"
#     school = "AkiraChix"
#For a class to accept instant variables we add the __init__ method /function to the class
#The __init__ method has double underscoresin eac side of the word init.
#The first argument of the init method is always called self.
#It must contain atleast one argument.
class Students:
    school = "AkiraChix"
    def __init__(self,age,country,first_name,last_name):
        self.age = age
        self.country = country 
        self.first_name = first_name
        self.last_name = last_name
       
    def full_name(self):
       full_name = self.first_name + " " + self.last_name
       return full_name.title()

    def greet(self):
        return f"Hello {self.full_name()} from {self.country} welcome to {self.school}"
        

    def year_of_birth(self):
        year_of_birth = 2022-int(self.age)
        return f"You were born in the year {year_of_birth}"

    def initials(self):
        initials = self.first_name[0] + " " + self.last_name[0]
        return f"Your initials are {initials.upper()}" 

effence = Students(age=22,country="Kenya",first_name="effence",last_name="waithera")
print(effence.full_name())
print(effence.greet())
print(effence.year_of_birth())
print(effence.initials())

susan = Students(age=23,country="Uganda",first_name="susan",last_name="nakimuli")
print(susan.full_name())
print(susan.greet())
print(susan.year_of_birth())
print(susan.initials())

#Add these methods to class student - full_name, year_of_birth, initials. Create two instances and verify the work as expected
