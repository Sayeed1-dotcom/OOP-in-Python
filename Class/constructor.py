#__init__ is a constructor by default in class.
#In every class there is always a constructor. __init __ is a constructor that actually used in class section to add attributes (like name,age,gender) for object.

class Student:
     # class.attributes
    college_name = "Chittagong International Medical College" 
         #constructor       
    def __init__(self,name,age,gender):
        self.name = name #obj.attributes
        self.age = age #obj.attributes
        self.gender = gender #obj.attributes

print(Student.college_name)
s1 = Student("Ahnat Afrn",22,"Female")
print(s1.name,s1.age,s1.gender)
# print(Student.college_name)

s2 = Student("Peyal Biswas",24,"Male")
print(s2.name,s2.age,s2.gender)
# print(Student.college_name)

s3 = Student("Nusrat Faria",22,"female")
print(s3.name,s3.age,s3.gender)
# print(Student.college_name)