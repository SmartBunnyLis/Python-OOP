class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk (self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Health is: ", self.health


animal1 = Animal ("dog" , 100)
animal1.walk().run().displayHealth()
animal1.walk().run().displayHealth()
animal1.walk().run().displayHealth()
# ========================================================================================
# dog

class Dog(Animal):
    def __init__(self, name, health = 150):
        super(Dog, self).__init__(name, health)
    
    def pet(self):
        self.health += 5
        return self


dog1 = Dog("Shadow", 160 )
print dog1.name, dog1.health
dog1.walk().run().pet().displayHealth()
dog1.walk().run().displayHealth()
dog1.walk().displayHealth()

# ======================================================================

class Dragon(Animal):
    def setHealth(self):
        self.health = 170
        return self
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "I am a Dragon & my Health is : ",self.health
        # return self


dragon1 = Dragon("Ali", 1000)
dragon1.setHealth().displayHealth()


