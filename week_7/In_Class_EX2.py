#2.1. The simplest class: (5 points)
#a)
class Simplest:
    pass
print(type(Simplest))
#b)
simp=Simplest()
print(type(simp))

#2.2. Person Class: (5 points)
class Person:
    first_name = ""
    last_name = ""
    middle_initials=""

    def fullname(self):
        return f"{self.first_name} {self.middle_initials} {self.last_name}"

person_a=Person()
person_a.first_name="Sivanand"
person_a.last_name="Sista"
person_a.middle_initials="K"
print(person_a.fullname())

#2.3. Cylinder: (5 points)
import math
class Cylinder:

    def set_height_radius(self, height, radius):
        self.height=height
        self.radius=radius

    def volume(self):
        return format(self.height*math.pi*(self.radius)**2,".2f")

    def surface_area(self):
        top=math.pi*(self.radius)**2
        return format(2*top+2*math.pi*self.radius*self.height,".2f")

mycyl = Cylinder()
mycyl.set_height_radius(2,3)
print(mycyl.volume())
print(mycyl.surface_area())
