class Computer:
    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling price:{}".format(self.maxprice))

    def setMaxprice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()


c.setMaxPrice(1000)
c.sell()
    