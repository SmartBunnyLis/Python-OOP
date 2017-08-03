class Car():
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000: 
            self.tax = self.price * 0.15 
        else:
            self.tax = self.price * 0.12
        
    def display_all(self):
        print "Price is", self.price
        print "Speed is", self.speed
        print "Fuel is", self.fuel
        print "Mileage is", self.mileage
        print "Tax is", self.tax

car1 = Car(5000, 200, "full", 30000)
car2 = Car(3000, 250, "full", 50000)
car3 = Car(24000, 230, "full", 30000)
car4 = Car(35000, 400, "full", 30000)
car5 = Car(45000, 500, "full", 30000)
car6 = Car(105000, 100, "full", 30000)
cars = [car1, car2, car3, car4, car5, car6]
        
for car in cars:
    car.display_all()    