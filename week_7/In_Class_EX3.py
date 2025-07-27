#3.1. NumberSet Class (5 points)
class NumberSet:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

t=NumberSet(6,10)
print(t.num1,t.num2)

#3.2. Animal Class (5 points)

class Animal:

    def __init__(self, arms, legs):
        self.arms = arms
        self.legs = legs

    def get_arms(self):
        return self.arms

    def get_legs(self):
        return self.legs

    def get_arms_legs(self):
        return self.arms+self.legs


spider=Animal(4,4)
print(spider.get_arms())
print(spider.get_legs())
spidlimbs=spider.get_arms_legs()
print(spidlimbs)

#3.3. Cereal Class (5 points)

class Cereal:
    """class called Cereal that accepts three inputs in the Ctor: 2 strings and 1
    integer, and assigns them to 3 instance variables in the constructor:
    name, brand, and fiber."""
    def __init__(self,name,brand,fiber):
        self.name = name
        self.brand = brand
        self.fiber=fiber

    def get_info(self):
        print("{} cereal is produced by {} and has {} grams of fiber in every serving.".format(self.name,self.brand,self.fiber))

c1=Cereal("Corn Flakes","Kellogg's",2)
c1.get_info()
c2=Cereal("Honey Nut Cheerios","General Mills",3)
c2.get_info()
