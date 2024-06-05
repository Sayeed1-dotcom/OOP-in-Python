#super() method used to access methods of parent class

class school:
    cname = "Chittagong International Medical & Dental College"     
    @staticmethod
    def type1():
        print('Medical College')

    @staticmethod  
    def type2():
        print('Dental College')

    def __init__(self,name,level,roll):
        self.name = name
        self.level = level
        self.roll = roll

class parents(school):

    def __init__(self,name,father,mother,level,roll):
        self.father = father
        self.mother = mother
         #super method
        super().__init__(name,level,roll)
        super().type2()

s1 = parents("Afrin Absar","Mohammad Absar","Zinnat Begum",13,11)
print(s1.cname)
print(s1.name)
print("class :",s1.level,'\n roll :',s1.roll)
print('father name:',s1.father,'\n mother name:',s1.mother)
