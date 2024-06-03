class Car:
    co_name = "Sayeed Group of Industries"
    
    def __init__(self,name,color,brand):
        self.name = name
        self.color = color
        self.brand = brand
    
    def welcome(self):
        print("Welcome Mr.", self.name)
    
    def get_color(self):
        return self.color
    
    def get_brand(self):
        return self.brand
        
print(Car.co_name)

c1 = Car("Sajib Hossain", "Green","BMW")
#print(c1.name,c1.color,c1.brand)
print("Your Car color is", c1.get_color())
print("Your Car manufactured by", c1.get_brand())
c1.welcome()

c2 = Car("Sayeed Mohammad", "matte black","Mercedes Benz")
#print(c2.name,c2.color,c2.brand)
print("Your Car color is", c2.get_color())
print("Your Car manufactured by", c2.get_brand())
c2.welcome()
