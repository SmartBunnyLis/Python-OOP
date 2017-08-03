class Product():
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "For Sale"
    
    def sell(self):
        self.status = "Sold"

    def tax(self, tax):
        self.price = self.price*tax
        return self.price

    def return_item(self, reason):
        self.reason = reason
        if (self.reason == "defective" ):
            self.status = "Defective"
            self.price = 0
        elif(self.reason == "In Box" ):
            self.status = "NEW !!! For Sale !!!"
        else:
            self.status = "USED"
            self.price = self.price - self.price*0.25
        return self

    def displayInfo(self):
        print self.price
        print self.item_name
        print self.weight,"lbs"
        print self.brand
        print self.cost
        print self.status

car1 = Product(100000, "Car", 3000, "Tesla", 5000)
car1.return_item("Muhahahah")
car1.displayInfo()



