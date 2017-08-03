class Bike():
    def __init__(self, price, max_speed):
        self.price=price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayInfo(self):
        print "Price is: ", self.price
        print "Speed is: ", self.max_speed
        print "Miles is: ", self.miles


    def ride(self):
        print "Riding"
        self.miles += 10
        # must return self
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        print "miles s",self.miles
        # return self for sure
        return self

bike1 = Bike(1000, 25)
bike2 = Bike(2000, 35)
bike2 = Bike(10000, 100)
bike1.ride()
bike1.ride()
bike1.ride()
# Reverse==================
bike1.reverse().displayInfo()