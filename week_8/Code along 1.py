# Week 8
# Code lab 1 part 1
class Animal:
    def __init__(self):
        print("Animal created")

    def whoamI(self):
        print("I am an Animal")

    def eat(self):
        print("I am now eating")

    def speak(self):
        raise NotImplementedError("Subclass not implemented")


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        print("Dog created")
        self.name=name

    def whoamI(self):
        print("I am a Dog, my name is",self.name)

    def eat(self):
        print("I am now eating")

    def speak(self):
        return self.name+" says woof!"

class Cat:
    def __init__(self,name):
        self.name=name

    def whoamI(self):
        print("I am a Cat, my name is",self.name)

    def eat(self):
        print("I am now eating")

    def speak(self):
        return self.name+" says meow!"

class Bird(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        print("Bird created")

    def whoamI(self):
        print("I am a Bird")

    def eat(self):
        print("I am now eating")

def pet_speak(pet):
    print(pet.speak())

# animal=Animal()
# animal.whoamI()
# animal.eat()
# animal.speak()



fido=Dog("Fido")
# fido.whoamI()
# fido.eat()
# fido.speak()



felix=Cat("Felix")
# felix.whoamI()
# felix.eat()
# felix.speak()
polly=Bird("Polly")
pet_speak(fido)
pet_speak(felix)
pet_speak(polly)