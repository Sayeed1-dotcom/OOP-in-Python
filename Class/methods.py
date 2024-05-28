#In class we write many functions, that is called method
#methods are functions in class that belongs to objects

class Student:
    #method 
    def welcome(self):
        print("Welcome dear", )

s1 = Student()
#to use method
s1.welcome()


#using methods with objects 
class Student:
                   
    def __init__(self,name,age,marks):
        self.name = name 
        self.age = age 
        self.marks = marks

    #method 
    def welcome(self):
        print("Welcome dear", self.name)

    #method
    def get_age(self):
        return self.age
    
    #method
    def get_marks(self):
        return self.marks
    
    

s1 = Student("Ahnat Afrn",22, 90)
print(s1.name,s1.age,s1.marks)
s1.welcome()
print("Your age is", s1.get_age())
print("You've got ", s1.get_marks())
