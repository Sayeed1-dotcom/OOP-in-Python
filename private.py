#we use underscore (__) to make attributes & methods private
class instagram:
    def __init__(self,id,password):
        self.id = id
        self.__password = password 

    #this method used to access private attributes 
    # def reset__pass(self):
        # return self.__password

id1 = instagram('Sayeed Mohammad', '123@idabc')

print(id1.id)
print(id1.__password)
# print(id1.reset__pass())
