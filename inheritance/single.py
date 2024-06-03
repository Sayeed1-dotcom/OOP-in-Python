class school:
    cname = "Chittagong International Medical & Dental College"

    @staticmethod
    def type1():
        print('Medical College')

    @staticmethod  
    def type2():
        print('Dental College')
        
class student(school):
    sname = "Afrin Absar"

    def __init__(self,level,roll ):
        self.level = level
        self.roll = roll


s1 = student(13,11)
print(s1.cname)
print(s1.type2())
print(s1.sname,'\n', s1.level, '\n', s1.roll)

