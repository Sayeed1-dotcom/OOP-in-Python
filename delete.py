#we use del keyword to delete objects or object properties
# del object (to delete object)
# del object.property (to delete object property)
class student:
    def __init__(self,name):
        self.name = name

s1 = student("Sayeed Mohammad")
print(s1)
print(s1.name)
del s1
print(s1)
del s1.name
print(s1.name)