'''
child class will override parent class method when we have same method
'''
# class GP:
#     def method(self):
#         print("This is grand parent class")
# class P:
#     def method(self):
#         print("this is parent class")
#
# class C(GP,P):
#     def method(self):
#         print("this is child class")
# obj1 = C()
# obj1.method()  # MRO concept


class Mobile:
    def __init__(self,price,modelNo):
        self.Price = price
        self.modelNo = modelNo
    def getPrice(self):
        return self.Price
    def discountPrice(self):
        return self.Price-self.Price*0.10
    def getModel(self):
        return self.modelNo

class Samsung(Mobile):
    def __init__(self,price,modelNo):
        Mobile.__init__(self,price,modelNo)
    def feature(self):
        print("this is best budget freindly mobile")
    def discountPrice(self):
        return self.Price - self.Price*0.20
class IPhone(Mobile):
    def __init__(self,price,modelNo):
        Mobile.__init__(self,price,modelNo)
    def feature(self):
        print("this is mose expensive mobile ")

samsung = Samsung(50000,10110)
print(samsung.discountPrice())









